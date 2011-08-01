import os
from django.utils.functional import lazy

# Django settings for ff4 project.

ROOT = os.path.dirname(os.path.abspath(__file__))

PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))
PROJECT_DIR = os.path.realpath(os.path.dirname(__file__))
path = lambda *a: os.path.join(ROOT, *a)

DATABASES = {}
DATABASE_ROUTERS = ('multidb.MasterSlaveRouter',)

CACHES = {}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/New_York'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-US'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

DBGETTEXT_PATH = PROJECT_PATH + '/locale'

# Tells the extract script what files to look for l10n in and what function
# handles the extraction. The Tower library expects this.
DOMAIN_METHODS = {
    # We usually use "messages" as text domain. "django" is required by Django L10n.
    'django': [
        # Normally, apps would be in apps/ and templates in templates/.
        # Not so here.
        ('things/**.py',
            'tower.management.commands.extract.extract_tower_python'),
        ('templates/**.html',
            'lib.shoehorn_l10n.tower_blocktrans.extract_django_template'),
        ('templates_orig/**.html',
            'lib.shoehorn_l10n.tower_blocktrans.extract_django_template'),
    ],
}
TOWER_KEYWORDS = {
    #'_lazy': None,
}
# The POT headers take care of the encoding.
TOWER_ADD_HEADERS = True

# Fake Jinja2 config for tower. Don't ask. (If you must, bug 647352).
def JINJA_CONFIG():
    return {'extensions': []}

# tower-ize django's blocktrans
import lib.shoehorn_l10n.templatetag
lib.shoehorn_l10n.templatetag.monkeypatch()

# Accepted locales on dev and prod.  Change these lists to control which
# locales are turned on on dev and prod.  Then, assign one of them to
# KNOWN_LANGUAGES below (or in settings_local).
KNOWN_LANGUAGES_DEV = (
    'en-US',
    'de',
    'es',
    'fr',
)

KNOWN_LANGUAGES_PROD = (
    'en-US',
    'de',
    'es',
    'fr',
)

# Accepted locales.  One of: KNOWN_LANGUAGES_DEV, KNOWN_LANGUAGES_PRODF
KNOWN_LANGUAGES = KNOWN_LANGUAGES_PROD

# List of RTL locales known to this project. Subset of LANGUAGES.
RTL_LANGUAGES = ('ar',)  # ('ar', 'fa', 'fa-IR', 'he')

LANGUAGE_URL_MAP = dict([(i.lower(), i) for i in KNOWN_LANGUAGES])

# Override Django's built-in with our native names
class LazyLangs(dict):
    def __new__(self):
        from django.conf import settings
        from product_details import product_details
        return dict([(lang.lower(), product_details.languages[lang]['native'])
                     for lang in settings.KNOWN_LANGUAGES])

LANGUAGES = lazy(LazyLangs, dict)()

# Where to store product details etc.
PROD_DETAILS_DIR = path('lib/product_details_json')

# Paths that don't require a locale prefix.
SUPPORTED_NONLOCALES = ('static', 'admin', 'robots.txt')

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = PROJECT_PATH + '/../static/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/static/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/static/admin/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'p&hhgrz+0ry9a8s(o34v=_nx*$=p-2fv1-x@lwu8%t%1ffi%$7'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'ff4.jinja.Loader',
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'commons.middleware.LocaleURLMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'ff4.urls'

TEMPLATE_DIRS = (
    PROJECT_PATH + '/templates_orig',
)

JINJA_TEMPLATE_DIRS = (
    PROJECT_PATH + '/templates',
)

def JINJA_CONFIG():
    import jinja2
    config = {'extensions': ['tower.template.i18n', 'jinja2.ext.loopcontrols',
                             'jinja2.ext.with_'],
              'finalize': lambda x: x if x is not None else ''}
    return config


TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
    'django.core.context_processors.i18n',
    'django.contrib.auth.context_processors.auth',
    'commons.context_processors.i18n',
)

SERIALIZATION_MODULES = {
    'yml': "django.core.serializers.pyyaml"
}

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'djcelery',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    'django.contrib.admindocs',
    'ff4.things',
    'south',
    'tower',
    'product_details',
)

FIXTURE_DIRS = (
    PROJECT_PATH + '/fixtures/',
)

SOUTH_TESTS_MIGRATE = False
FIREFOX_DOWNLOAD_URL = "http://www.mozilla.com/en-US/firefox/?WT.mc_ID=webifyme"

# Directories to create snapshots, thumbnails, etc. in.
SHARED_IMG_DIR = os.path.join(MEDIA_ROOT, 'collages')
SNAPSHOT_BASE = os.path.join(SHARED_IMG_DIR, 'snapshots/')
THUMB_BASE = os.path.join(SHARED_IMG_DIR, 'thumbs_gallery/')
FEATURED_THUMB_BASE = os.path.join(SHARED_IMG_DIR, 'thumbs_featured/')

SHARED_IMG_URL = ''.join((MEDIA_URL, 'collages/'))
SNAPSHOT_BASE_URL = SHARED_IMG_URL + 'snapshots/'
THUMB_BASE_URL = SHARED_IMG_URL + 'thumbs_gallery/'
FEATURED_THUMB_BASE_URL = SHARED_IMG_URL + 'thumbs_featured/'

LOG_FILENAME = "%s/render_collage.log" % PROJECT_PATH
RESPONSYS = ''
RESPONSYS_API_URL = ''
CURRENT_SITE = ''
COLLAGES_URL = ''

# Should robots.txt deny everything or disallow a calculated list of URLs we
# don't want to be crawled?  Default is false, disallow everything.
# Also see http://www.google.com/support/webmasters/bin/answer.py?answer=93710
ENGAGE_ROBOTS = False
