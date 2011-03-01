import sys, os
sys.path.append(os.path.join(os.path.realpath(os.path.dirname(__file__)),'..','..','..'))

from django.core.management import setup_environ
from ff4 import settings
setup_environ(settings)

import beanstalkc, json, logging
from django.conf import settings
from PIL import Image, ImageOps
from ff4.things.models import Collage
from ff4.things.backgrounds import BACKGROUNDS

LOG_FILENAME = 'render_collage.log'
logging.basicConfig(level=logging.ERROR,
                    format='%(asctime)s :: %(levelname)s %(message)s',
                    filename=LOG_FILENAME,
                    filemode='w')


CANVAS_WIDTH = 875
CANVAS_HEIGHT = 600
BOX_SIZE = 25

STATIC_PATH = settings.MEDIA_ROOT

# we can just use the default pipe...
while True:
    job = settings.BEANSTALK.reserve()
    jobStats = job.stats()
    
    col = Collage.objects.get(slug=job.body)
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

    col.filename = job.body + '.jpg'
    try:
        canvasGalleryThumb = canvas.resize((190, 143), Image.ANTIALIAS)
        canvasGalleryThumb.save(STATIC_PATH + 'collages/thumbs_gallery/' + col.filename)
        canvasFeaturedThumb = canvas.resize((190, 143), Image.ANTIALIAS)
        canvasFeaturedThumb.save(STATIC_PATH + 'collages/thumbs_featured/' + col.filename)
        canvas.save(STATIC_PATH + 'collages/' + col.filename)
    except:
        logging.error("Problem saving the final image. job #" + str(jobStats['id']) + " buried. slug=" + str(job.body))
        job.bury()
    
    col.save()
    print "Image saved: " + col.filename + "\n"
    job.delete()
