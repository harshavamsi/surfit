import os

from surfit.settings.base import *

DEBUG = True





# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases




STATIC_ROOT = os.environ.get('STATIC_ROOT', None)
