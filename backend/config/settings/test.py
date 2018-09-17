from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'risko_test',
        'USER': 'postgres',
        'PASSWORD': '12345678',
        'HOST': 'localhost',
    }
}


