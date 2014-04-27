from os import path

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'database.db',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': ''
    }
}

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'bambu_ajax',
    'testproject.myapp'
)

SECRET_KEY = 'sm8apo4(o4ni9n=nsn7-3x8g@fkeuckm(#ixpk5lw3vrzq*ads'
ROOT_URLCONF = 'testproject.urls'

TEMPLATE_LOADERS = (
	'django.template.loaders.filesystem.Loader',
	'django.template.loaders.app_directories.Loader',
)

SITE_ROOT = path.abspath(path.dirname(__file__) + '/../')
STATIC_ROOT = path.join(SITE_ROOT, 'static')
TEMPLATE_DIRS = (
	path.join(SITE_ROOT, 'templates'),
)