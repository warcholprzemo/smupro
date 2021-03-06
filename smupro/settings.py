"""
Django settings for smupro project.

Generated by 'django-admin startproject' using Django 2.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import dj_database_url
import django_heroku
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'f7qt5!2n)!=7%#(9xy&1$-j)#k16sbozh!d)4sv=#0g+v(&+6h'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['shielded-beach-87349.herokuapp.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'multiplex',
    'pocket',
    'tictactoe',

    'django_filters',
    'rest_framework',
    'corsheaders',
    'storages',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    #'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'corsheaders.middleware.CorsPostCsrfMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'spa.middleware.SPAMiddleware',
]

ROOT_URLCONF = 'smupro.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'build'), os.path.join(BASE_DIR, 'prod-template')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'smupro.wsgi.application'


DATABASES = {'default': dj_database_url.config()}

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'pl'

TIME_ZONE = 'Europe/Warsaw'

USE_I18N = True

USE_L10N = True

USE_TZ = True

#ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'


STATICFILES_DIRS = [
     os.path.join(BASE_DIR, "dist"),  # copy files from here into staticfiles (WhiteNoiseMiddleware likes it!)
]

CORS_ORIGIN_WHITELIST = (
    '127.0.0.1:3000',
    'localhost:3000',
    'localhost:8080',
)

REST_FRAMEWORK = {
    # Use Djnago's standard `django.contrib.auth` permissions
    # or allow read-only access for unauthoricated users.
    #'DEFAULT_PERMISSION_CLASSES': [
    #    'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    #],
}

# Activate Django-Heroku.
django_heroku.settings(locals(), staticfiles=False)

AWS_DEFAULT_ACL = None
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = 'warcholprzemo-bucket'
AWS_S3_HOST = 's3.eu-west-2.amazonaws.com'
AWS_S3_CUSTOM_DOMAIN = "%s.%s" % (AWS_STORAGE_BUCKET_NAME, AWS_S3_HOST)
STATICFILES_STORAGE = 'smupro.s3utils.StaticRootS3BotoStorage'
STATIC_URL = "%s%s%s" % ('https://', AWS_STORAGE_BUCKET_NAME, '.s3.amazonaws.com/static/')

DEFAULT_FILE_STORAGE = 'smupro.s3utils.MediaRootS3BotoStorage'
MEDIA_URL = "%s%s%s" % ('https://', AWS_STORAGE_BUCKET_NAME, '.s3.amazonaws.com/media/')

try:
    from .local_settings import *
except ImportError:
    pass

if DEBUG:
    INSTALLED_APPS += [
        'django.contrib.admin',
    ]
    del DEFAULT_FILE_STORAGE
