
import os
import datetime
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-1eg9#%h6y$e-f&w+80jc-i)5#)55qn(h8g0u%#%)qvmq@06#vm'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'crispy_forms',
    'authentication',
    'products_api',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',]

CORS_ORIGIN_ALLOW_ALL = True #configure This

ROOT_URLCONF = 'MisuiIndia.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'MisuiIndia.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# DATABASES = {
#         'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#         }
#     }


DATABASES = {
        'default': {
            'ENGINE': 'djongo',
            'NAME': 'codefree',
            'ENFORCE_SCHEMA': False,
            'CLIENT': {
                'host': 'mongodb+srv://sourav:sourav@cluster0.cdasj.mongodb.net/codefree?retryWrites=true&w=majority'
            }  
        }
}
# mongodb+srv://sourav:<password>@cluster0.cdasj.mongodb.net/myFirstDatabase?retryWrites=true&w=majority
# DATABASES = {
#         'default': {
#             'ENGINE': 'djongo',
#             'NAME': 'dropit',
#             'ENFORCE_SCHEMA': False,
#             'CLIENT': {
#                 'host': 'mongodb+srv://sourav:sourav@cluster0.cdasj.mongodb.net/codefree?retryWrites=true&w=majority'
#             }  
#         }
# }

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'authentication.CustomUser'
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': datetime.timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': datetime.timedelta(days=100),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': False,
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUTH_HEADER_TYPES': ('JWT',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
}



# from datetime import timedelta
# SIMPLE_JWT = {
#   'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
#   'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
#   'ROTATE_REFRESH_TOKENS': False,
#   'BLACKLIST_AFTER_ROTATION': True,
#   'UPDATE_LAST_LOGIN': False,

#   'ALGORITHM': 'HS256',
#   'SIGNING_KEY': SECRET_KEY,
#   'VERIFYING_KEY': None,
#   'AUDIENCE': None,
#   'ISSUER': None,

#   'AUTH_HEADER_TYPES': ('Bearer',),
#   'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
#   'USER_ID_FIELD': 'id',
#   'USER_ID_CLAIM': 'user_id',
#   'USER_AUTHENTICATION_RULE': 'rest_framework_simplejwt.authentication.default_user_authentication_rule',

#   'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
#   'TOKEN_TYPE_CLAIM': 'token_type',

#   'JTI_CLAIM': 'jti',

#   'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
#   'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
#   'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),

#   # custom
#   'AUTH_COOKIE': 'access_token',  # Cookie name. Enables cookies if value is set.
#   'AUTH_COOKIE_DOMAIN': None,     # A string like "example.com", or None for standard domain cookie.
#   'AUTH_COOKIE_SECURE': False,    # Whether the auth cookies should be secure (https:// only).
#   'AUTH_COOKIE_HTTP_ONLY' : True, # Http only cookie flag.It's not fetch by javascript.
#   'AUTH_COOKIE_PATH': '/',        # The path of the auth cookie.
#   'AUTH_COOKIE_SAMESITE': 'Lax',  # Whether to set the flag restricting cookie leaks on cross-site requests. This can be 'Lax', 'Strict', or None to disable the flag.
# }



# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# STATIC_URL = '/static/'
# MEDIA_URL = '/media/'
# CORS_ORIGIN_ALLOW_ALL = True
# CORS_ALLOW_CREDENTIALS = True
# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# MEDIA_ROOT = os.path.join(BASE_DIR, 'static')


STATIC_URL = '/static/'

MEDIA_URL = '/media/'


STATIC_ROOT  =    os.path.join(BASE_DIR, 'static')


MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True