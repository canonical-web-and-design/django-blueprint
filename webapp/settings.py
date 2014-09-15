"""
Django settings for canonical project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Keep it secret, keep it safe!
SECRET_KEY = 'o@kjnphb9#+3fl80i#$v$+0la3u^atow)b33h*bafbcwir0w04'

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
TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

# See http://tinyurl.com/django-context-processors
TEMPLATE_CONTEXT_PROCESSORS = [
    "django.core.context_processors.static",  # {{ STATIC_URL }}
    "django_asset_server_url.asset_server_url",  # {{ ASSET_SERVER_URL }}
]
