from .base import *


DEBUG = os.getenv('PROD_DEBUG')

ALLOWED_HOSTS = os.getenv('PROD_ALLOWED_HOSTS')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_PASSWORD'),
        'PORT': os.getenv('DB_PORT')
        }
    }
