from django.db import models
from django.utils.translation import ugettext as _
from django.template.defaultfilters import slugify
import hashlib
from datetime import datetime
from django.conf import settings
from things.questions_answers import *

class QuizQuestion(models.Model):
    slug = models.SlugField(blank=True) # default max length (50)

    def save(self):
        self.slug = slugify( hashlib.md5( QUESTIONS[self.pk] + datetime.now().strftime("%Y%m%d%H%m%s") ).hexdigest()[:12] )
        super( QuizQuestion, self ).save()

    def __unicode__(self):
        return unicode(QUESTIONS[self.pk])

class QuizAnswer(models.Model):
    slug = models.SlugField(unique=True)
    quiz_question = models.ForeignKey(QuizQuestion)

    def save(self):
        self.slug = slugify( ANSWERS[self.pk] )
        super( QuizAnswer, self ).save()

    def __unicode__(self):
        return unicode(ANSWERS[self.pk])

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

    def save(self):
        if self.slug == "":
            self.slug = slugify( hashlib.md5(self.username + datetime.now().strftime("%Y%m%d%H%m%s") ).hexdigest()[:12]  )
        super( Collage, self ).save()


    def __unicode__(self):
        return self.filename

    def snapshot_url(self):
        if self.filename:
          return settings.SNAPSHOT_BASE_URL + self.filename[:2] + '/' + self.filename
        return None

