from shopifyApp.settings.base import *
MIDDLEWARE.append('shopifyApp.middleware.dev_cors_middleware')
DEBUG = True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
        'USER': '',
    }
}
