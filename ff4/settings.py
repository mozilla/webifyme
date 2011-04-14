import settings_local
import os
import beanstalkc

# Django settings for ff4 project.

DEBUG = settings_local.DEBUG
DEV = settings_local.DEV
TEMPLATE_DEBUG = DEBUG

PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))
PROJECT_DOMAIN = ''
PROJECT_DIR = os.path.realpath(os.path.dirname(__file__))

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',       # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': settings_local.DB_NAME,             # Or path to database file if using sqlite3.
        'USER': settings_local.DB_USER,             # Not used with sqlite3.
        'PASSWORD': settings_local.DB_PASSWORD,     # Not used with sqlite3.
        'HOST': settings_local.DB_HOST,             # Set to empty string for localhost. Not used with sqlite3.
        'PORT': settings_local.DB_PORT,             # Set to empty string for default. Not used with sqlite3.
    }
}

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

# Accepted locales
INPUT_LANGUAGES = ('ar', 'bg', 'ca', 'cs', 'da', 'de', 'el', 'en-US', 'es',
                   'fr', 'fy-NL', 'gl', 'he', 'hu', 'id', 'it', 'ko', 'nb-NO',
                   'nl', 'pl', 'pt-PT', 'ro', 'ru', 'sk', 'sq', 'uk', 'vi',
                   'zh-CN', 'zh-TW')
RTL_LANGUAGES = ('ar', 'he',)  # ('fa', 'fa-IR')
# Fallbacks for locales that are not recognized by Babel. Bug 596981.
BABEL_FALLBACK = {'fy-nl': 'nl'}

DBGETTEXT_PATH = PROJECT_PATH+'/locale'


# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = PROJECT_PATH+'/../static/'

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
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
)

ROOT_URLCONF = 'ff4.urls'

TEMPLATE_DIRS = (
    PROJECT_PATH+'/templates_orig',
)

JINJA_TEMPLATE_DIRS = (
    PROJECT_PATH+'/templates',
)

def JINJA_CONFIG():
    import jinja2
    config = {'extensions': ['jinja2.ext.loopcontrols',
                             'jinja2.ext.with_', 'caching.ext.cache'],
              'finalize': lambda x: x if x is not None else ''}
    return config


TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
    'django.core.context_processors.i18n',
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
    # Uncomment the next line to enable the admin:
    #'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'south',
    'dbgettext',
    'ff4.things',
)

FIXTURE_DIRS = (
    PROJECT_PATH+'/fixtures/',
)
SOUTH_TESTS_MIGRATE = False

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST =  settings_local.EMAIL_HOST
EMAIL_PORT = settings_local.EMAIL_PORT
EMAIL_HOST_USER = settings_local.EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = settings_local.EMAIL_HOST_PASSWORD
EMAIL_USE_TLS = settings_local.EMAIL_USE_TLS

BEANSTALK = beanstalkc.Connection(settings_local.BEANSTALK_HOST, settings_local.BEANSTALK_PORT)

FIREFOX_DOWNLOAD_URL = "http://www.mozilla.com/en-US/firefox/" #False # set this on download day to change 'Get Download Day' reminder links to 'Download Firefox 4' links

SNAPSHOT_BASE_URL = '/static/collages/'


BITLY_USERNAME = settings_local.BITLY_USERNAME
BITLY_APIKEY = settings_local.BITLY_APIKEY