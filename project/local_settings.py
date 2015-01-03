from os import path

BASE_DIR = path.dirname(path.dirname(__file__))
PROJECT_ROOT = path.dirname(__file__)

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = path.join(BASE_DIR, 'media')
STATIC_ROOT = path.join(PROJECT_ROOT, 'static')
STATICFILES_DIRS = (
    path.join(BASE_DIR, 'static'),
)