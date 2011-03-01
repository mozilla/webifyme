import os, sys, math
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from PIL import Image, ImageOps
from ff4.things import models

class Command(BaseCommand):

    def handle(self, *args, **options):
        
        
        object_path = os.path.join(settings.MEDIA_ROOT, 'objects')
        medium_img_path = os.path.join(object_path,'medium')
        
        print 'Saving sizes...'
        
        for image in models.Image.objects.all():
            try:
                img = Image.open(os.path.join(medium_img_path,image.file_name))
            except IOError:
                print "%s missing" % image.file_name
                continue # ignore images that don't exist
            
            width, height = img.size
            
            image.width = width
            image.height = height
            image.save()
            #print "%s saved" % png_name
            
