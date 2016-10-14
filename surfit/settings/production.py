import os

from surfit.settings.base import *

DEBUG = False

ALLOWED_HOSTS = ['surfit.maayafest.com','mithril.maayafest.com','localhost']





# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': '/home/curious/surfit_db.cnf',
        },
    }
}


STATIC_ROOT = os.environ.get('STATIC_ROOT', None)
