"""
Django settings for MVA project.

Generated by 'django-admin startproject' using Django 5.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""
import os
from pathlib import Path
from environs import Env
import dj_database_url
from pytz import timezone

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

env = Env()
env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str('SECRET_KEY')
EXTERNAL_SECRET_KEY = env.str('EXTERNAL_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DEBUG', default=False)

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=[])  # if not running_tests() else []

IS_PRODUCTION_ENV = env.bool('IS_PRODUCTION_ENV')
IS_REMOTE_DB = env.bool('IS_REMOTE_DB', default=False)


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'django.contrib.sites',
    'django.contrib.postgres',

    # Apps
    'apps.api',
    'apps.core',
    'apps.users',
    'apps.integration',

    # Custom
    'debug_toolbar',
    'nested_admin',
    'mptt',
    'trix_editor',
    'django_ckeditor_5',
    # 'sslserver',
    'corsheaders',
    'admin_reorder',
    'extra_settings',
    'django_json_widget',
    'django_celery_results',

    # Rest Framework
    'rest_framework',
    'rest_framework_api_key',
    'drf_yasg',
    # 'rest_framework.authtoken',
    # 'dj_rest_auth',s

    # oauth
    'oauth2_provider',
    'social_django',  # python social auth
    'drf_social_oauth2',

    # *** django-categories ***
    # 'categories',
    # 'categories.editor',
    # 'django_elasticsearch_dsl'
]

ADMIN_REORDER = (
    # Authorization
    {'app': 'users',
     'models': (
         'users.User',
         'auth.Group',
     )},

    # Core
    {'app': 'core',
     'label': 'Core',
     'models': (
         'core.DataHistory',
         'core.PotentialFranchise',
         'core.Contact',
     )},

    # integration
    {'app': 'integration',
     'label': 'integration',
     'models': (
        'integration.MainPage',
        'integration.ContactPage',
        'integration.EstimationPage',
        'integration.Franchises',
        'integration.Article',
        'integration.BlogPage',
        'integration.PoliticsPage',
        'integration.CookiesPage',
        'integration.MentionPage',
     )},

    {'app': 'extra_settings',
     'label': 'extra_settings',
     'models': (
         'extra_settings.Setting',
     )},

    # Celery
    {'app': 'django_celery_results',
     'label': 'Celery Results',
     'models': (
         'django_celery_results.TaskResult',
     )},


    # Keep original label and models
    # 'oauth2_provider',
    # 'social_django',
    'rest_framework_api_key',
    'sites',

    # {'app': 'django_oauth_toolkit',
    #  'label': 'django_oauth_toolkit',
    #  'models': (
    #      'django_oauth_toolkit.Setting',
    #  )},
)

MIDDLEWARE = [
    # 'mva_proj.middleware.PrerenderMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'admin_reorder.middleware.ModelAdminReorder',

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'social_django.middleware.SocialAuthExceptionMiddleware',
]

CORS_ALLOW_ALL_ORIGINS = True  # Allow all origins

ROOT_URLCONF = 'mva_proj.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',
            BASE_DIR / 'apps/core/templates',
            BASE_DIR / 'apps/users/templates'
        ]
        ,
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

WSGI_APPLICATION = 'mva_proj.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        # 'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        # 'ENGINE': 'django.db.backends.mysql',
        'NAME': env.str('DB_NAME'),
        'USER': env.str('DB_USER'),
        'PASSWORD': env.str('DB_PASS'),
        'HOST': env.str('DB_HOST'),
        'PORT': env.int('DB_PORT'),
    }
}

if IS_REMOTE_DB:
    DATABASES['default'] = dj_database_url.config(
        default=f"postgres://{env.str('REMOTE_DB_USER')}:{env.str('REMOTE_DB_PASS')}@{env.str('REMOTE_DB_HOST')}:"
                f"{env.str('REMOTE_DB_PORT')}/{env.str('REMOTE_DB_NAME')}",
        conn_max_age=600
    )


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'public/static/')

if IS_PRODUCTION_ENV:
    STATICFILES_DIRS = (  # TODO: manage static files
        # "/home/mva/mva/frontend/build/static",
        # "/home/mva/mva/frontend/public",
    )

MEDIA_URL = 'public/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'public/media/')

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# ---------------------------------------------------
DOMAIN = env.str('DOMAIN')
FRONTEND_URL = env.str('FRONTEND_URL')
BACKEND_URL = env.str('BACKEND_URL')
SENDER = env.str('SENDER')
# SendGrid
SENDGRID_API_KEY = env.str('SENDGRID_API_KEY')
# Regexp
RE_POSITIVE_INTEGER_OR_FLOAT = r'^(?:[1-9]\d*|0)?(?:\.\d+)?$'
RE_POSITIVE_INTEGER = r'^(?:[1-9]\d*|0)?$'
RE_NUMBER = r'^(?:[0-9]\d*)?$'
# ----------------------------------------------------
LAZY_SESSION_ID_KEY = 'lsid'
SITE_ID = 1

AUTH_USER_MODEL = 'users.User'
DATA_UPLOAD_MAX_NUMBER_FIELDS = 10000

CORS_ORIGIN_ALLOW_ALL = True  # Allowing all origins is not recommended for production

CORS_ORIGIN_WHITELIST = [
    'http://127.0.0.1:3000',
    'http://192.168.0.107:3000',
    'http://localhost:3000',
    'http://206.81.17.158:3000',
    'http://206.81.17.158:8000',
    "https://vroommarket.fr",
    "https://www.vroommarket.fr",
    # Add more allowed origins as needed
]

CSRF_TRUSTED_ORIGINS = [
    'https://vroommarket.fr',
    'https://www.vroommarket.fr',
    'http://127.0.0.1:3000',
    'http://206.81.17.158:3000',
]

# Account settings
# from another lib
LOGIN_URL = '/admin/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_URL = '/admin/logout/'
LOGOUT_REDIRECT_URL = '/'

# The exact details of how a user is mapped from the social provider’s user to yours, and associated with existing users,
# are specified by the SOCIAL_AUTH_PIPELINE
#
# define a custom social auth pipeline.
# The key thing here is to include email association. Both FB and Google
# only return validated user emails, so email validation is safe.
#
# Don't do this if you wish to use an OAuth2 provider which doesn't
# validate email addresses, as that opens up an attack vector.
# An attacker targeting one of your users might create an account with
# the OAuth2 provider, falsely claiming your user's email address as
# their own. Without validation, that provider can't know otherwise.
# They can then gain access to your user's account by logging in via
# that OAuth2 provider.
#
# See here for more details:
# http://psa.matiasaguirre.net/docs/use_cases.html#associate-users-by-email
SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.social_auth.associate_by_email',  # <- this line's not included by default
    'social_core.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
)

AUTHENTICATION_BACKENDS = (
    # Others auth providers (e.g. Facebook, OpenId, etc)
    # ...

    # Facebook OAuth2
    'social_core.backends.facebook.FacebookAppOAuth2',
    'social_core.backends.facebook.FacebookOAuth2',

    # Google OAuth2
    'social_core.backends.google.GoogleOAuth2',
    # ------------------------------------------------

    # drf-social-oauth2
    'drf_social_oauth2.backends.DjangoOAuth2',

    # Django
    'django.contrib.auth.backends.ModelBackend',
)

# Allow SVG files
from django.core.files.uploadhandler import MemoryFileUploadHandler, TemporaryFileUploadHandler

FILE_UPLOAD_HANDLERS = [
    "django.core.files.uploadhandler.MemoryFileUploadHandler",
    "django.core.files.uploadhandler.TemporaryFileUploadHandler",
]

# Extend allowed file types
import mimetypes
mimetypes.add_type("image/svg+xml", ".svg", True)


# Celery settings
CELERY_BROKER_URL = 'redis://localhost:6379'
# CELERY_RESULT_BACKEND = "redis://localhost:6379"
CELERY_RESULT_BACKEND = 'django-db'

CELERY_timezone = "UTC"
CELERY_task_serializer = "json"
CELERY_result_expires = 600
CELERY_accept_content = ('application/json',)  # 'application/x-yaml'
#
# CELERY_max_memory_per_child=None
CELERY_worker_cancel_long_running_tasks_on_conncetion_loss = True

# result_backend = 'db+postgresql://scott:tiger@localhost/mydatabase'

# CELERY_CACHE_BACKEND = 'default'
# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
#         'LOCATION': 'cache',
#     }
# }

DJANGO_CELERY_RESULTS_TASK_ID_MAX_LENGTH = 191

CKEDITOR_5_CONFIGS = {
    'default': {
        'toolbar': {
            'items': [
                'heading', '|', 'bold', 'italic', 'link',
                'bulletedList', 'numberedList', 'blockQuote', 'imageUpload'  # Добавляем imageUpload
            ],
        },
        'heading': {
            'options': [
                { 'model': 'paragraph', 'title': 'Paragraph', 'class': 'ck-heading_paragraph' },
                { 'model': 'heading1', 'view': 'h1', 'title': 'Heading 1', 'class': 'ck-heading_heading1' },
                { 'model': 'heading2', 'view': 'h2', 'title': 'Heading 2', 'class': 'ck-heading_heading2' },
                { 'model': 'heading3', 'view': 'h3', 'title': 'Heading 3', 'class': 'ck-heading_heading3' },
                { 'model': 'heading4', 'view': 'h4', 'title': 'Heading 4', 'class': 'ck-heading_heading4' },
                { 'model': 'heading5', 'view': 'h5', 'title': 'Heading 5', 'class': 'ck-heading_heading5' },
                { 'model': 'heading6', 'view': 'h6', 'title': 'Heading 6', 'class': 'ck-heading_heading6' }
            ]
        },
        'list': {
            'properties': {
                'styles': True,  # Разрешить стили списков
                'startIndex': True,  # Разрешить указание индекса начала списка
                'reversed': True,  # Разрешить реверс списка
            }
        },
        'image': {
            'toolbar': [
                'imageTextAlternative', '|', 'imageStyle:full', 'imageStyle:side', '|', 'resizeImage', '|', 'imageUpload'
            ],
        },
        'imageUpload': {
            # Настроить серверный путь для загрузки изображений (зависит от вашего серверного окружения)
            'url': 'media/upload/',  # Пример для Django
        }
    },
}
CKEDITOR_5_FILE_UPLOAD_PERMISSION = "staff"  # Possible values: "staff", "authenticated", "any"
CKEDITOR_5_FILE_STORAGE = "mva_proj.storages.CustomStorage"  # optional

# OAUTH2 Settings
from oauth2_provider import settings as oauth2_settings
# oauth2_settings.DEFAULTS['ACCESS_TOKEN_GENERATOR'] = 'mva_proj.token_management.token_generator'

# Django logging
from .extra_settings.django.logging import *  # noqa
# Django mailing
from .extra_settings.django.email import *  # noqa
# Debug Toolbar
from .extra_settings.third_party.debug_toolbar import *  # noqa
# DRF
from .extra_settings.third_party.drf import *  # noqa


# ******************* SOCIALS ************************

# YouTube
from .extra_settings.third_party.google import *  # noqa
# Facebook
from .extra_settings.third_party.facebook import *  # noqa
# Instagram
from .extra_settings.third_party.instagram import *  # noqa