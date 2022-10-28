from .base import *
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

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
#

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR,'static']

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR,'media'
#

# EMAIL SETTINGS
# EMAIL_USE_TLS = True
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_HOST_USER = get_secret('EMAIL')
# EMAIL_HOST_PASSWORD = get_secret('PASS_EMAIL')
# EMAIL_PORT = 587