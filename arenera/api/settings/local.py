from .base import*


DEBUG = True

ALLOWED_HOSTS = []


DATABASES = {
      'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'arenera',
        'USER': 'root',
        'PASSWORD': 'Dedlr2406!',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}


STATIC_URL = 'static/'