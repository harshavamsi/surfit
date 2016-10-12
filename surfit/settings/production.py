import os

from surfit.settings.base import *

DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1']

ALLOWED_HOSTS += [os.environ['DJANGO_HOST_NAME']]

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases




STATIC_ROOT = os.environ.get('STATIC_ROOT', None)
