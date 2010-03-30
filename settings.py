# -*- coding: utf-8 -*-

_ = lambda s: s

import os.path

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
PROJECT_NAME = os.path.split(PROJECT_ROOT)[-1]



# DEBUGGING

DEBUG = False
TEMPLATE_DEBUG = DEBUG
INTERNAL_IPS = ('127.0.0.1', )



# CACHE

CACHE_BACKEND = 'locmem://'
CACHE_MIDDLEWARE_KEY_PREFIX = '%s_' % PROJECT_NAME
CACHE_MIDDLEWARE_SECONDS = 600



# EMAIL / ERROR NOTIFY

SERVER_EMAIL = 'pb@philippbosch.de'
ADMINS = (
    ('Philipp Bosch', 'philipp.bosch@me.com'),
)
MANAGERS = ADMINS



# DATABASE

DATABASE_ENGINE = 'mysql'
DATABASE_NAME = PROJECT_NAME
DATABASE_USER = 'root'
DATABASE_PASSWORD = ''
DATABASE_HOST = ''
DATABASE_PORT = ''



# I18N

TIME_ZONE = 'Europe/Berlin'
LANGUAGE_CODE = 'en'
LANGUAGES = (
    ('en', 'English'),
)
USE_I18N = True



# URLS

SITE_ID = 1
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')
MEDIA_URL = '/media/'
ADMIN_MEDIA_PREFIX = '/admin-media/'
ROOT_URLCONF = '%s.urls' % PROJECT_NAME
# PREPEND_WWW = True



# APPS, MIDDLEWARES, CONTEXT PROCESSORS

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    # 'django.contrib.csrf',
    'south',
    'compressor',
    'reversion',
    'sorl.thumbnail',
    'tinymce',
    
    'cms',
    'cms.plugins.text',
    'cms.plugins.picture',
    'cms.plugins.link',
    'cms.plugins.file',
    'menus',
    'mptt',
    'publisher',
    
    'jonnsonaguirre.works',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
    'django.core.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'cms.context_processors.media',
)



# TEMPLATE LOADING

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates'),
)
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
    'django.template.loaders.eggs.load_template_source',
)



# SECRET

try:
    SECRET_KEY
except NameError:
    SECRET_FILE = os.path.join(PROJECT_ROOT, 'secret.txt')
    try:
        SECRET_KEY = open(SECRET_FILE).read().strip()
    except IOError:
        try:
            from random import choice
            SECRET_KEY = ''.join([choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50)])
            secret = file(SECRET_FILE, 'w')
            secret.write(SECRET_KEY)
            secret.close()
        except IOError:
            Exception('Please create a %s file with random characters to generate your secret key!' % SECRET_FILE)



# Override the server-derived value of SCRIPT_NAME 
# See http://code.djangoproject.com/wiki/BackwardsIncompatibleChanges#lighttpdfastcgiandothers
FORCE_SCRIPT_NAME = ''



# SOUTH

SOUTH_AUTO_FREEZE_APP = True



# DJANGO-CSS

COMPRESS = True
COMPILER_FORMATS = {
    '.sass': {
        'binary_path': 'sass -t compressed',
        'arguments': '*.sass *.css',
    }
}
COMPRESS_OUTPUT_DIR = 'compressed'



# DJANGO-CMS

CMS_TEMPLATES = (
        ('default.html', _('default')),
)
CMS_TEMPLATE_INHERITANCE = False
CMS_PERMISSION = False
CMS_MODERATOR = False
CMS_SHOW_START_DATE = False
CMS_SHOW_END_DATE = False
CMS_URL_OVERWRITE = False
CMS_REDIRECTS = False
CMS_SEO_FIELDS = False
CMS_SOFTROOT = False



# TINYMCE

TINYMCE_DEFAULT_CONFIG = {
    'plugins': "paste",
    'theme': "advanced",
    'custom_shortcuts': False,
    'object_resizing': False,
    'theme_advanced_blockformats': "p,h2,h3",
    'theme_advanced_toolbar_location': "top",
    'theme_advanced_toolbar_align': "left",
    'theme_advanced_buttons1': "bold,underline,separator,justifyleft,justifycenter,justifyright,justifyblock,separator,bullist,numlist,separator,undo,redo,separator,formatselect,styleselect,removeformat,cleanup,separator,link,unlink,separator,code",
    'theme_advanced_buttons2': "",
    'theme_advanced_buttons3': "",
    'theme_advanced_styles': "Big=big;Small=small",
    'content_css': MEDIA_URL + 'css/screen.css',
}



# SORL THUMBNAIL

THUMBNAIL_QUALITY = 75



# ISSUU

ISSUU_API_KEY = 'qmym5codqqfmyygnbke1l5ekesglow8b'
ISSUU_API_SECRET = 'pngwenubvboo6nfeucfzly36z94st8wg'



# LOCAL SETTINGS

try:
    execfile(os.path.join(os.path.dirname(__file__), "settings_local.py"))
except IOError:
    pass
