"""
Django settings for this project
"""

# Go to http://www.miniwebtool.com/django-secret-key-generator/
# And generate a secret key to put here
SECRET_KEY = ''

# See https://docs.djangoproject.com/en/dev/ref/contrib/
INSTALLED_APPS = [
    'django_versioned_static',
    'django_collectstatic_disabled'
]

ALLOWED_HOSTS = ['*']

MIDDLEWARE_CLASSES = []

ROOT_URLCONF = 'webapp.urls'
WSGI_APPLICATION = 'webapp.wsgi.application'
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = False
USE_L10N = True
USE_TZ = True
STATIC_ROOT = 'static'
STATIC_URL = '/static/'
STATICFILES_FINDERS = ['django_static_root_finder.StaticRootFinder']
TEMPLATE_DIRS = ['templates']

# See http://tinyurl.com/django-context-processors
TEMPLATE_CONTEXT_PROCESSORS = [
    "django.core.context_processors.static",  # {{ STATIC_URL }}
    "django_asset_server_url.asset_server_url",  # {{ ASSET_SERVER_URL }}
]

import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
