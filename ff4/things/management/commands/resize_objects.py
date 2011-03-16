import os, sys, math
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from PIL import Image, ImageOps
from ff4.things import models

class Command(BaseCommand):
    args = '<percent scale_name save_size>'

    def handle(self, *args, **options):
        if len(args) < 2:
            raise CommandError('Requires percent and scale name.')
        
        scale_factor = float(args[0])/100.0
        scale_name = args[1]
        
        save_size = False
        
        if len(args) >= 3:
            #if save_size is specifed, the created image size will get saved to the db
            save_size = bool(int(args[2]))
        
        object_path = os.path.join(settings.MEDIA_ROOT, 'objects')
        full_img_path = os.path.join(object_path,'full')
        scaled_img_path = os.path.join(object_path,scale_name)
        
        
        if not os.path.isdir(scaled_img_path):
            print 1
        
        print 'Resizing images by %f...' % scale_factor
        
        for image in models.Image.objects.all():
            try:
                img = Image.open(os.path.join(full_img_path,image.file_name))
            except IOError:
                print "%s missing" % image.file_name
                continue # ignore images that don't exist
            
            width, height = img.size
            width = int(math.floor(float(width) * scale_factor))
            height = int(math.floor(float(height) * scale_factor))
            
            img_out = img.resize((width,height), Image.ANTIALIAS)
            #img_out.convert("RGBA")
            png_name = image.file_name.rsplit('.',1)[0] + '.png'
            img_out.save(os.path.join(scaled_img_path, png_name),"PNG")
            
            # now that that's all set, update the db
            if save_size:
                image.width = width
                image.height = height
                image.save()
            #print "%s saved" % png_name
            
