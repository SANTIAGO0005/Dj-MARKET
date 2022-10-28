from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'marketdb',
        'USER': 'Django',
        'PASSWORD': '1q2w3e4r5t',
        'HOST': 'localhost',
        'PORT': '7000',
    }
}