"""
Django project settings
"""

# A static site has no need of a secure secret key
# since the key is only used for signing sessions, password hashes, etc.
# none of which have any place in a static site

SECRET_KEY = 'SECRET_KEY_INSECURE_PLACEHOLDER'  # !! CHANGE ME !!

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
