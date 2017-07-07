from shopifyApp.settings.base import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'myproject',
        'USER': 'myuser',
        'PASSWORD': 'bestpasswordever',
    }
}
