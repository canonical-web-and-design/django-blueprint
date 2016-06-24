"""
Django project settings
"""

import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Although the insecure, easily guessed SECRET_KEY
# 'SECRET_KEY_INSECURE_PLACEHOLDER' *will work* with Django,
# you *should* change it when you get the chance.
# E.g. from http://www.miniwebtool.com/django-secret-key-generator/
#
# While this static-django-bootstrap app is only being used as intended -
# to serve essentially static templates with no dynamic functionality,
# an insecure SECRET_KEY won't introduce any insecurities in the application.
#
# However, as soon as you start using sessions, passwords, crypto functions
# or anything that uses django.utils.crypt.get_random_string(),
# you will need a strong SECRET_KEY to ensure your app remains secure
# (see: http://stackoverflow.com/a/15383766/613540)
SECRET_KEY = 'SECRET_KEY_INSECURE_PLACEHOLDER'  # !! CHANGE ME !!

ALLOWED_HOSTS = ['*']
DEBUG = False

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = False
USE_L10N = False
USE_TZ = False

WSGI_APPLICATION = 'webapp.wsgi.application'
ROOT_URLCONF = 'webapp.urls'
APPEND_SLASH = False
REMOVE_SLASH = True
STATIC_ROOT = "static"
STATIC_URL = '/static/'

WHITENOISE_MAX_AGE = 31557600
WHITENOISE_ALLOW_ALL_ORIGINS = False

# See https://docs.djangoproject.com/en/dev/ref/contrib/
INSTALLED_APPS = [
    'django.contrib.staticfiles',
    'django_versioned_static_url'
]

MIDDLEWARE_CLASSES = [
    'unslashed.middleware.RemoveSlashMiddleware',
]

STATICFILES_FINDERS = [
    'django_static_root_finder.finders.StaticRootFinder'
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django_asset_server_url.asset_server_url',
            ],
        },
    },
]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'error_file': {
            'level': 'ERROR',
            'filename': os.path.join(BASE_DIR, 'django-error.log'),
            'class': 'logging.handlers.RotatingFileHandler',
            'maxBytes': 1 * 1024 * 1024,
            'backupCount': 2
        }
    },
    'loggers': {
        'django': {
            'handlers': ['error_file'],
            'level': 'ERROR',
            'propagate': True
        }
    }
}
