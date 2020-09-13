import os
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

DEBUG = 'runserver' in sys.argv

ADMINS               = [('jj', 'jj@returntothesource.nl')]
SERVER_EMAIL         = 'moniquebroekman@rtts.eu'
MANAGERS             = ADMINS
ROOT_URLCONF         = 'mbcms.urls'
WSGI_APPLICATION     = 'mbcms.wsgi.application'
SESSION_SERIALIZER   = 'django.contrib.sessions.serializers.JSONSerializer'
SECRET_KEY           = 'ml$$+w*5#+n%f^1ifmxaixk^^j7a2#7)gk%3f7-tl1)cvwxg_+'
STATIC_ROOT          = '/srv/moniquebroekman/static'
STATIC_URL           = "/static/"
STATICFILES_DIRS     = [os.path.join(PROJECT_DIR, 'static')]
ALLOWED_HOSTS        = ['localhost', 'www.moniquebroekman.nl', 'moniquebroekman.nl']
TIME_ZONE            = 'Europe/Amsterdam'
LANGUAGE_CODE        = 'nl'
SITE_ID              = 1
USE_I18N             = True
USE_L10N             = True
USE_TZ               = True
MEDIA_ROOT           = '/srv/moniquebroekman/media'
MEDIA_URL            = "/media/"
CKEDITOR_UPLOAD_PATH = "/srv/moniquebroekman/media"

INSTALLED_APPS = [
    'ckeditor',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    #'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'embed_video',
    'website',
    'portfolio',
    'blog',
    'cms', # new!
]
if not DEBUG:
    INSTALLED_APPS += ['django.contrib.staticfiles']

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(PROJECT_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

MIDDLEWARE = [
    'django.middleware.cache.UpdateCacheMiddleware',
    'cms.middleware.SassMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    #'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cms.middleware.FetchFromCacheMiddleware',
]

CKEDITOR_CONFIGS = {
    'default': {
        'autoGrow_onStartup': True,
        'forcePasteAsPlainText': True,
        'contentsCss': '/static/editor.css', # sorry, should've computed this
        'toolbar_Full': [
            ['Format', 'Bold', 'Italic', 'Underline', 'RemoveFormat'],
            ['Anchor', 'Link', 'Image', 'Blockquote', 'Table', 'HorizontalRule'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent'],
            ['Find', 'Replace', 'Scayt'],
            ['Source'],
            ],
        'toolbar': 'Full',
        'height': 400,
        'width': '100%',
        'allowedContent': True, # this allows iframes, embeds, scripts, etc...
        }
    }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'moniquebroekman',
        'USER': 'moniquebroekman',
    }
}
