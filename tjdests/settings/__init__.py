"""
Django settings for tjdests project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import logging
import os
import sys
from pathlib import Path
from typing import List, Optional

from django.contrib.messages import constants as messages

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-7nju0o%j&gz7&v^05iuq*tn$_iwvtjh1cq26@is(u2d4snkum5"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS: List[str] = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "crispy_forms",
    "crispy_bootstrap5",
    "social_django",
    "django_extensions",
    "bootstrap_pagination",
    "axes",
    "tjdests.apps.authentication",
    "tjdests.apps.destinations",
    "tjdests.apps.profile",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "axes.middleware.AxesMiddleware",
]

ROOT_URLCONF = "tjdests.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "tjdests.apps.context_processors.settings_renderer",
            ],
        },
    },
]

WSGI_APPLICATION = "tjdests.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

AUTH_USER_MODEL = "authentication.User"

AUTHENTICATION_BACKENDS = (
    "axes.backends.AxesStandaloneBackend",
    "tjdests.apps.authentication.oauth.IonOauth2",
    "django.contrib.auth.backends.ModelBackend",
)

AXES_LOCKOUT_CALLABLE = "tjdests.apps.authentication.views.lockout"
MAINTAINER = ""

SOCIAL_AUTH_REDIRECT_IS_HTTPS = False
SOCIAL_AUTH_ION_KEY = ""
SOCIAL_AUTH_ION_SECRET = ""


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "serve/")
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static/"),)

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

LOGIN_REDIRECT_URL = "authentication:tos"
LOGOUT_REDIRECT_URL = "authentication:index"

LOGIN_URL = "authentication:login"

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

MESSAGE_TAGS = {
    messages.ERROR: "danger",
}

TESTING = any("test" in arg for arg in sys.argv)
if TESTING:
    AXES_ENABLED = False

# Override the following in secret.py
SENIOR_GRAD_YEAR: int = -1
BRANDING_NAME: str = "UNDEFINED"
GLOBAL_MESSAGE: Optional[str] = None
LOGIN_LOCKED = False

try:
    from .secret import *  # noqa  # pylint: disable=unused-import
except ImportError:
    logging.warning("Error importing secret.py")
