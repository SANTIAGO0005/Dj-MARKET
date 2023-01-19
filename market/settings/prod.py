from .base import *
import dj_database_url
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*','https://market-site-app.onrender.com']

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
}

TATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR,'static']

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR,'media'