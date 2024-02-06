from .base import *

DEBUG = os.getenv('DEV_DEBUG')

ALLOWED_HOSTS = os.getenv('DEV_ALLOWED_HOSTS')

DATABASES = {
    'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
