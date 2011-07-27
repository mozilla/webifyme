import json
import random
import string
import pycurl
from django.core import serializers
from django.core.paginator import Paginator
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.utils.encoding import force_unicode
from django.utils import translation
from django.utils.translation import ugettext_lazy as _lazy
from django.utils.translation import ugettext as _
from django.utils.translation import ngettext
from django.views.decorators.cache import cache_page
from django.conf import settings
from django.contrib.sites.models import Site
from django.utils.http import urlencode

from commons.urlresolvers import reverse
from ff4.utils.render import render_response
from ff4.utils import bitly
from ff4.utils.bonus_objects import *
from ff4.utils.questions import get_question_JSON, serialize_image_list
from ff4.things.models import QuizQuestion, QuizAnswer, Collage, QuizAnswerByImage, Image
from ff4.things.backgrounds import BACKGROUNDS
from ff4.things.forms import QuizForm, DownloadForm
from things.questions_answers import *
from things.images import *
from ff4.things import tasks
from ff4.things.responsys import *


COLLAGE_SLUG_SESSION_KEY = 'owns_collage'

@cache_page(60 * 30)
def home(request):
    featured_collages = Collage.objects.filter(featured=True, in_gallery=True)[:3]
    if not featured_collages:
        featured_collages = Collage.objects.filter(in_gallery=True)[:3]
    context = {'featured_collages': featured_collages, 'current_url': urlencode({ 'href': settings.CURRENT_SITE })}
    return render_response(request, 'things/home.html', context)

@cache_page(30)
def gallery(request, page=1, chapter=1, featured=False):
    chapter = int(chapter)
    pages_per_chapter = 8
    collages_per_page = 8

    featured = True if featured else False
    collages = Collage.objects.all().order_by('-id').filter(in_gallery=True, featured=featured)

    total = collages.count()
    start_range = ((chapter - 1) * pages_per_chapter * collages_per_page)
    end_range = start_range + (pages_per_chapter * collages_per_page)

    if total > end_range:
        more = True
    else:
        more = False

    featured_collages = collages[start_range:end_range]
    if not featured_collages:
        raise Http404

    pages = Paginator(featured_collages, 8)
    current_page = pages.page(page)

    context = {'featured_collages': current_page, 'page_object': pages, 'chapter': chapter, 'pages_per_chapter': pages_per_chapter, 'more': more, 'featured': featured, 'current_url': urlencode({ 'href': settings.CURRENT_SITE })}

    if request.is_ajax():
        return render_response(request, 'things/_gallery_page.html', context)
    else:
        return render_response(request, 'things/gallery.html', context)

@cache_page(30)
def gallery_nav(request, page=1, chapter=1, featured=False):

    chapter = int(chapter)

    pages_per_chapter = 8
    collages_per_page = 8

    featured = True if featured else False
    collages = Collage.objects.all().order_by('-id').filter(in_gallery=True, featured=featured)

    total = len(collages)
    start_range = ((chapter - 1) * pages_per_chapter * collages_per_page)
    end_range = start_range + (pages_per_chapter * collages_per_page)

    if total > end_range:
        more = True
    else:
        more = False

    featured_collages = collages[start_range:end_range]
    if not featured_collages:
        raise Http404

    pages = Paginator(featured_collages, 8)

    current_page = pages.page(page)

    context = {'featured_collages': current_page, 'page_object': pages, 'chapter': chapter, 'pages_per_chapter': pages_per_chapter, 'more': more, 'current_url': urlencode({ 'href': settings.CURRENT_SITE })}

    return render_response(request, 'things/_gallery_navigation.html', context)


def collage(request, slug='0'):

    try:
        collage = Collage.objects.get(slug=slug)  # grab the collage record
    except Collage.DoesNotExist:    # if there isn't one
        raise Http404               # throw a 404 for now, this'll be a rare problem

    # Need to expand the image coordinates data to include descriptions
    coords_json = json.loads(collage.images_coords)
    for coord in coords_json["objects"]:
        if not coord['img']:
            continue
        coord['name'] = force_unicode(IMAGES[coord['img']])
        coord['description'] = force_unicode(ANSWERS_BY_IMAGE[coord['id']])

    current_site = settings.CURRENT_SITE
    site_url = current_site
    current_url = urlencode({ 'href': site_url + settings.COLLAGES_URL + '/' + slug + '/' })
    url_for_bitly = site_url + settings.COLLAGES_URL + '/' + slug + '/'

    is_owner = False
    if COLLAGE_SLUG_SESSION_KEY in request.session and request.session[COLLAGE_SLUG_SESSION_KEY] == collage.slug:
        is_owner = True

    if request.is_ajax():
        changed = False  # keep track of any changes that might have happened
        # if we're getting an ajax request, then we're receiving our lovely collage data
        data = request.POST.items()     # and it's gonna come from a post request

        currentCoords = json.loads(collage.images_coords)
        if not collage.packed:  # only do packing if collage isn't already packed
            currentCoords['packed'] = True
            for key, value in data:
                if not key in ['scale', 'background']:
                    newValue = value.split(',')
                    try:
                        image_id = int(key)
                        x = int(newValue[0])
                        y = int(newValue[1])
                    except ValueError:
                        continue  # ignore non integer keys and values

                    for img in currentCoords['objects']:
                        if img['id'] == image_id:
                            img['x'] = x
                            img['y'] = y
                            break
                elif key == 'scale' and value in ['small', 'medium', 'large']:
                    currentCoords['scale'] = value

            collage.packed = True           # and tell us that it has been fixed
            changed = True

        if is_owner and 'background' in request.POST:  # only update the background is the owner of the collage is changing it
            background_class = request.POST.get('background', None)
            if background_class in [bg['class_name'] for bg in BACKGROUNDS]:  # ensure this is a valid background class
                collage.background_img = background_class
                currentCoords['background'] = background_class
                changed = True

        if changed:
            collage.filename = ''  # clear out any old snapshot filename
            collage.images_coords = json.dumps(currentCoords)
            collage.save()                  # and save the record back to the db

            if settings.DEBUG == True:
                tasks.run_debug(str(slug))
            else:
                tasks.run.delay(slug=(str(slug)))  # queue up the job for render_collage to pick up

        return HttpResponse(slug)
		
    # generate bitly url
    if not collage.bitly_url:
		if not bitly.BITLY_BASE_URL.lower().startswith('https://'):
		    raise Exception('Bitly API URL must start with HTTPS.')
		curl = pycurl.Curl()
		curl.setopt(pycurl.SSL_VERIFYPEER, 1)
		curl.setopt(pycurl.SSL_VERIFYHOST, 2)
		curl.setopt(pycurl.URL, bitly.BITLY_BASE_URL)
        try:
            curl.perform()
            api = bitly.Api(settings.BITLY_USERNAME, settings.BITLY_APIKEY)
            bitly_url = api.shorten(url_for_bitly)
        except bitly.BitlyError:
            pass
        else:
            collage.bitly_url = bitly_url
            collage.save()

    collage.images_coords = json.dumps(coords_json)

    context = {'collage': collage, 'is_owner': False}
    if is_owner:
        context['backgrounds'] = json.dumps(BACKGROUNDS)
        context['is_owner'] = True

    context['current_url'] = current_url
    context['current_site'] = current_site
    context['site_url'] = site_url
    context['bitly_url'] = collage.bitly_url

    return render_response(request, 'things/collage.html', context)

@cache_page(60 * 30)
def collage_snapshot(request, slug):
    try:
        collage = Collage.objects.get(slug=slug)  # grab the collage record
    except Collage.DoesNotExist:    # if there isn't one
        raise Http404               # throw a 404 for now, this'll be a rare problem

    if collage.snapshot_url():
        if request.is_ajax():
            return HttpResponse(json.dumps({'url': collage.snapshot_url()}))
        else:
            return HttpResponseRedirect(collage.snapshot_url())
    raise Http404


def quiz_json():
    questions = []
    for question in QuizQuestion.objects.select_related('quizanswer_set').all():
        lang_specific_question = _(force_unicode(QUESTIONS()[question.pk]))
        quest_left = 1,
        data = {
            'id': question.id,
            # L10n: {0} is the number of questions remaining in the quiz
            'progress': ngettext('{0} more to go', '{0} more to go', quest_left),
            'question': lang_specific_question,
            'answers': []
        }
        for answer in question.quizanswer_set.all():
            lang_specific_answer = _(force_unicode(ANSWERS()[answer.pk]))
            data['answers'].append({'answer': lang_specific_answer, 'id': answer.id})
        questions.append(data)
    return json.dumps(questions)

def images_json():
    images = []
    for image in Image.objects.order_by('?').all()[:5]:
        lang_specific_name = force_unicode(IMAGES[image.file_name])
        data = {
            'file_name': image.file_name,
            'width': image.width,
            'height': image.height,
            'name': force_unicode(IMAGES[image.file_name])
        }
        images.append(data)
    return json.dumps(images)


def download_reminder(request):
    if request.method == 'POST':
        form = DownloadForm(request.POST)

        if not form.is_valid():
            return HttpResponse(_("Error saving your email address"))

        if form.cleaned_data['email']:
            subscribe('MOZILLA_AND_YOU', form.cleaned_data['email'])

    return HttpResponse("success")


def quiz(request):
    if request.method == 'POST':        # if we're posting, then our quiz is completed
        form = QuizForm(request.POST)   # clean the data submitted via the form at the end of the quiz
        if not form.is_valid():
            return HttpResponse(_("Error saving the collage."))

        if form.cleaned_data['email']:
            subscribe('MOZILLA_AND_YOU', form.cleaned_data['email'])

        queryList = []                          # create a list for our answers to query images

        for question_id, answer_id in request.POST.items():       # go through all our items
            try:
                queryList.append(int(answer_id))            # and build a list for the query to the QuizAnswerByImage table
            except ValueError:
                pass  # ignore non integer values

        images = QuizAnswerByImage.objects.select_related('image').filter(answer__in=queryList)  # get all the images that match these answers

        # reorg images by answer_id, this is presumably faster than 28 separate queries
        answer_groups = {}
        for image in images:
            if not image.answer_id in answer_groups:
                answer_groups[image.answer_id] = []
            answer_groups[image.answer_id].append(image)

        image_map = {}  # store images in a map, keyed on their id, to avoid duplicates
        for answer_id, images in answer_groups.items():
            image = images[random.randint(0, len(images) - 1)]  # pick a random image from the group
            image_map[image.image.id] = {'id': image.image.id, 'img': image.image.file_name, 'width': image.image.width, 'height': image.image.height}

        # get country specific object
        country_code = translation.get_language()[:2]
        country_object = get_country_object(country_code)
        if country_object:
            country_image = Image.objects.get(file_name=country_object['file_name'])
            if country_image:
                image_map[country_image.id] = {'id': country_image.id, 'img': country_image.file_name, 'width': country_image.width, 'height': country_image.height}

        # get browser specific object
        browser_object = get_browser_object(request.META['HTTP_USER_AGENT'])
        if browser_object:
            browser_image = Image.objects.get(file_name=browser_object['file_name'])
            if browser_image:
                image_map[browser_image.id] = {'id': browser_image.id, 'img': browser_image.file_name, 'width': browser_image.width, 'height': browser_image.height}

        # get community object
        community_object = get_community_object(request.session.get('HTTP_REFERER'))
        if community_object:
            community_image = Image.objects.get(file_name=community_object['file_name'])
            if community_image:
                image_map[community_image.id] = {'id': community_image.id, 'img': community_image.file_name, 'width': community_image.width, 'height': community_image.height}

        # get email easter egg object
        easter_egg_object = get_easter_egg(form.cleaned_data.get('email', 'anonymous'))
        if easter_egg_object:
            easter_egg_image = Image.objects.get(file_name=easter_egg_object['file_name'])
            if easter_egg_image:
                image_map[easter_egg_image.id] = {'id': easter_egg_image.id, 'img': easter_egg_image.file_name, 'width': easter_egg_image.width, 'height': easter_egg_image.height}

        random_bg_class = BACKGROUNDS[random.randint(0, len(BACKGROUNDS) - 1)]['class_name']
        jsonObj = {'packed': False, 'background': random_bg_class, 'objects': image_map.values()}  # pack it up
        jsonString = json.dumps(jsonObj)  # serialize the dump
        collage = Collage(images_coords=jsonString, username=form.cleaned_data.get('username', 'Anonymous'), featured=False, background_img=random_bg_class, in_gallery=form.cleaned_data.get('gallery_include', False))
        try:
            collage.save()
            #assign this user as the owner of this collage
            request.session[COLLAGE_SLUG_SESSION_KEY] = collage.slug
            #redirect to collage
            return HttpResponseRedirect('/collage/' + collage.slug + '/')
        except:
            return HttpResponse(_("Error saving the collage"))
    return render_response(request, 'things/question.html', ({'quiz_json': quiz_json(), 'images_json': images_json(), 'current_url': urlencode({ 'href': settings.CURRENT_SITE })}))

@cache_page(60 * 30)
def features(request):
    return render_response(request, 'things/features.html')
