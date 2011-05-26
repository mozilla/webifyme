from celery.task import task

import sys, os
sys.path.append(os.path.join(os.path.realpath(os.path.dirname(__file__)),'..','..','..'))

from django.core.management import setup_environ
from ff4 import settings
setup_environ(settings)

import json, logging
from django.conf import settings
from PIL import Image, ImageOps
from ff4.things.models import Collage
from ff4.things.backgrounds import BACKGROUNDS

logging.basicConfig(level=logging.ERROR,
                    format='%(asctime)s :: %(levelname)s %(message)s',
                    filename=settings.LOG_FILENAME,
                    filemode='w')

CANVAS_WIDTH = 875
CANVAS_HEIGHT = 600
BOX_SIZE = 25
STATIC_PATH = settings.MEDIA_ROOT

def process_collage(slug):

    col = Collage.objects.get(slug=slug)
    images_coords = json.loads(col.images_coords)

    # load the background image and paste it in
    bg_img = 'none.png'
    for bg in BACKGROUNDS:
        if bg['class_name'] == images_coords['background']:
            bg_img = bg['scaled']
            break
    try:
        canvas = Image.open(STATIC_PATH + 'backgrounds/scaled/' + bg_img)
    except IOError:
        canvas = Image.open(STATIC_PATH + 'backgrounds/scaled/none.png') # use the default background if the regular background can't be opened

    box = (0, 0, CANVAS_WIDTH, CANVAS_HEIGHT)
    canvas = canvas.crop(box)

    images = images_coords['objects']

    for i in images:
        if 'x' in i:
            try:
                fpo_obj = Image.open(STATIC_PATH + 'objects/' + images_coords['scale'] + '/' + i['img'])
            except IOError:
                logging.error("Problem opening " + 'objects/' + images_coords['scale'] + '/' + i['img'] + ". Skipping.")
                continue
            box = ( BOX_SIZE*i['x'], BOX_SIZE*i['y'], BOX_SIZE*i['x'] + fpo_obj.size[0], BOX_SIZE*i['y'] + fpo_obj.size[1])
            canvas.paste(fpo_obj, box, fpo_obj)

    col.filename = slug + '.jpg'
    try:       
        snapshot_dir = STATIC_PATH + settings.SNAPSHOT_BASE + slug[:2]
        thumb_dir = STATIC_PATH + settings.THUMB_BASE + slug[:2]
        featured_dir = STATIC_PATH + settings.FEATURED_THUMB_BASE + slug[:2]
        if not os.path.exists(snapshot_dir):
            os.mkdir(snapshot_dir)
        if not os.path.exists(thumb_dir):
            os.mkdir(thumb_dir)
        if not os.path.exists(featured_dir):
            os.mkdir(featured_dir)
        # Regular thumbs are 192 x 144 and are used in the gallery 
        canvasGalleryThumb = canvas.resize((192, 144), Image.ANTIALIAS)
        canvasGalleryThumb.save(thumb_dir + '/' + col.filename)
        # Featured thumbs are 216 x 162 and are used on the homepage
        canvasFeaturedThumb = canvas.resize((216, 162), Image.ANTIALIAS)
        canvasFeaturedThumb.save(featured_dir + '/' + col.filename)
        # full size images are 875 x 600 and are used for the download snapshot links
        canvas.save(snapshot_dir + '/' + col.filename)
    except:
        logging.error("Problem saving the final image: slug=" + slug, sys.exc_info()[0])
        raise

    col.save()


@task
def run(slug):
    process_collage(slug)

def run_debug(slug):
    process_collage(slug)

