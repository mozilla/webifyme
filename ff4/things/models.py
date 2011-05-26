from django.db import models
from django.utils.translation import ugettext as _
from django.template.defaultfilters import slugify
import hashlib
from datetime import datetime
from django.conf import settings
from things.questions_answers import *
import copy
import random

class QuizQuestion(models.Model):
    slug = models.SlugField(blank=True) # default max length (50)

    def save(self):
        self.slug = slugify( hashlib.md5( QUESTIONS( )[self.pk] + datetime.now().strftime("%Y%m%d%H%m%s") ).hexdigest()[:12] )
        super( QuizQuestion, self ).save()

    def __unicode__(self):
        return unicode(QUESTIONS( )[self.pk])

class QuizAnswer(models.Model):
    slug = models.SlugField(unique=True)
    quiz_question = models.ForeignKey(QuizQuestion)

    def save(self):
        self.slug = slugify( ANSWERS( )[self.pk] )
        super( QuizAnswer, self ).save()

    def __unicode__(self):
        return unicode(ANSWERS( )[self.pk])

class Image(models.Model):
    slug = models.SlugField(unique=True)
    file_name = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    width = models.IntegerField(default=50)
    height = models.IntegerField(default=50)
    locale = models.CharField(max_length=2, null=True, blank=True)

    def get_area(self):
        return int(self.width * self.height)

    def save(self):
        self.slug = slugify( self.file_name )
        super( Image, self ).save()

    def __unicode__(self):
        return self.file_name


class QuizAnswerByImage(models.Model):
    image = models.ForeignKey(Image)
    answer = models.ForeignKey(QuizAnswer)

class Collage(models.Model):
    slug = models.SlugField(unique=True)
    packed = models.BooleanField(default=False)
    images_coords = models.TextField(null=True, blank=True) # json object for computed collage
    background_img = models.CharField(max_length=50, default='wood.jpg')
    username = models.CharField(max_length=50)
    featured = models.BooleanField()
    in_gallery = models.BooleanField()
    filename = models.CharField(max_length=75)
    bitly_url = models.CharField(max_length=75, null=True, blank=True)

    username.verbose_name = "Title"
    
    def save(self):
        if self.slug == "":
            self.slug = self.generate_slug()
        super( Collage, self ).save()

    def generate_slug(self):
        return slugify( hashlib.md5(self.username + str(random.randint(0,100000)) + datetime.now().strftime("%Y%m%d%H%m%s") ).hexdigest()[:12] )

    def __unicode__(self):
        return self.filename

    def clone(self):
        """Return an identical copy of the instance with a new ID."""
        if not self.pk:
            raise ValueError('Instance must be saved before it can be cloned.')
        duplicate = copy.copy(self)
        # Setting pk to None tricks Django into thinking this is a new object.
        duplicate.pk = None
        duplicate.id = None
        duplicate.slug = self.generate_slug()
        duplicate.save()
        # ... but the trick loses all ManyToMany relations.
        for field in self._meta.many_to_many:
            source = getattr(self, field.attname)
            destination = getattr(duplicate, field.attname)
            for item in source.all():
                destination.add(item)
        return duplicate

    def snapshot_url(self):
        if self.filename:
          return settings.SNAPSHOT_BASE_URL + self.filename[:2] + '/' + self.filename
        return None

    def thumbnail_image_path(self):
        return self.snapshot_url()

    #dunno if I should have a template for this. Might be overkill?
    def thumbnail_image(self):
        return '<img src="%s" class="thumb">' % self.thumbnail_image_path()

    thumbnail_image.allow_tags = True

