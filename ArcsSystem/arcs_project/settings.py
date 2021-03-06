"""
Django settings for arcs_project project.

Generated by 'django-admin startproject' using Django 2.2.10.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""
from django.utils.translation import gettext_lazy as _ # This is needed to gather the strings of languages available on the site

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'bre=h5g+29%aw6&cpwbn9b75&ei&-=h_*c3778rcd9j%avnp-g' # TODO extract to environment variable

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True # TODO extract to environment variable

### use domain name not IP address for security
ALLOWED_HOSTS = ['localhost','127.0.0.1','dev.medborgarforskning.se', 'medborgarforskning.se']

# Application definition

INSTALLED_APPS = [
    'modeltranslation', # for Django 1.7 and above must be prior to django.contrib.admin - https://django-modeltranslation.readthedocs.io/en/latest/installation.html#required-settings
    'django.contrib.admin',
    'django.contrib.auth', # Core authentication framework and its default models. Required by AllAuth.
    'django.contrib.contenttypes', # Django content type system (allows permissions to be associated with models).
    'django.contrib.sessions',
    'django.contrib.messages', # also required by AllAuth
    'django.contrib.staticfiles',
    'django.contrib.sitemaps', # enables django to generate sitemap


### ArcsCore apps
    'blog', # enables the blog app of ArcsCore
    'publications', # enables the oublications app of ArcsCore
    #'products', #try to get rid of this one
    'projects', # enables the projects app of ArcsCore
    'staticpages',
    'workpackages',
    'organizations',

### Custom user apps
    'users', # initializes CustomUser and users app a.k.a. "People app" of ArcsCore

### Third party apps
    'django_summernote', # Installing summernote (CK)
    'taggit', # for handling tags/keywords (CK)

### AllAuth for social authentications start #
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.orcid',
### AllAuth for social authentications end #

### Wagtail app requirement start #
    'wagtail.contrib.forms',
    'wagtail.contrib.redirects',
    'wagtail.embeds',
    'wagtail.sites',
    'wagtail.users',
    'wagtail.snippets',
    'wagtail.documents',
    'wagtail.images',
    'wagtail.search',
    'wagtail.admin',
    'wagtail.core',

    'modelcluster',
    #'taggit', # I disabled this because we have it above (CK)
    'wagtail.contrib.modeladmin', # for wagtail menus
    'wagtailmenus', # initialize wagtail menus
### Wagtail app requirement end #
### Wagtail forms install #
    #'wagtail.wagtailforms',
### Wagtail forms install end #
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware', # Manages sessions across requests
    'django.middleware.locale.LocaleMiddleware', # local must be placed before CommonMiddleware as it needs an activated language. CacheMiddleware if used should be before Locale - https://docs.djangoproject.com/en/2.2/topics/i18n/translation/#how-django-discovers-language-preference
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware', # Associates users with requests using sessions.
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ### Wagtail app requirement start #
    'wagtail.core.middleware.SiteMiddleware',
    'wagtail.contrib.redirects.middleware.RedirectMiddleware',
    ### Wagtail app requirement end #
]

ROOT_URLCONF = 'arcs_project.urls'

# More on Template Configuration https://docs.djangoproject.com/en/2.2/topics/templates/
# This configuration currently has a common templates directory being referred to outside the app directory for the templates.
# Templates will also be looked for in each app's directory
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates/')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request', # `allauth` needs this from django
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz', # adds TIME_ZONE variable to RequestContext
                'wagtailmenus.context_processors.wagtailmenus',
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)

WSGI_APPLICATION = 'arcs_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# TODO replace sqlite3 with postgresql
#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql_psycopg2',
#        'NAME': 'myproject',
#        'USER': 'myprojectuser',
#        'PASSWORD': 'password',
#        'HOST': 'localhost',
#        'PORT': '',
#    }
#}
DATABASES = { # TODO switch to postgres
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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

#if ENVIRONMENT == 'production': # TODO: enable for production - though reverse proxy helps configure on this too
#    SECURE_BROWSER_XSS_FILTER = UserAttributeSimilarityValidator
#    X_FRAME_OPTIONS = 'DENY'
#    SECURE_SSL_REDIRECT = True
#    SECURE_HSTS_SECONDS = 31536000
#    SECURE_HSTS_INCLUDE_SUBDOMAIN = True
#    SECURE_HSTS_PRELOAD = False # TODO seto to true
#    SECURE_CONTENT_TYPE_NOSNIFF = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True


### Internationalization Start ###
# https://docs.djangoproject.com/en/2.2/topics/i18n/

#_ = lambda s: s # required per statement for django-modeltranslation https://django-modeltranslation.readthedocs.io/en/latest/installation.html#required-settings

LANGUAGE_CODE = 'en-us' # Default language used if no translation is available - ie language found in the templates

# For organization and resadability order alphabetically according to two letter language code
LANGUAGES = [
    ('en', _('English')), # The sublanguages like en-us can also be stated to differentiate translations
    ('sv', _('Swedish')),
]

LANGUAGE_CODES = [
    'en-us',
    'sv'
]

TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

### Internationalization End ###

### AllAuth Config ###
# Configuration options: https://django-allauth.readthedocs.io/en/latest/configuration.html
# Setting comments are a combination of the AllAuth settings example and added clarifying text.

#Account adapters
#ACCOUNT_ADAPTER = 'arcsauthenticator.adapter.CustomProcessAdapter' # specifies the adapter to modify default behavior else DefaultAccountAdapter

#all-auth registraion settings

# Specifies the login method to use -- whether the user logs in by entering
# their username, e-mail address, or either one of both. Possible values
# are 'username' | 'email' | 'username_email'
ACCOUNT_AUTHENTICATION_METHOD = "username_email"

# The URL to redirect to after a successful e-mail confirmation, in case no
# user is logged in. Default value is settings.LOGIN_URL.
# ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL

# The URL to redirect to after a successful e-mail confirmation, in case of
# an authenticated user. Default is settings.LOGIN_REDIRECT_URL
# ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL

# Determines the expiration date of email confirmation mails (# of days).
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 1

# The user is required to hand over an e-mail address when signing up.
ACCOUNT_EMAIL_REQUIRED = True

# Determines the e-mail verification method during signup. When set to
# "mandatory" the user is blocked from logging in until the email
# address is verified. Choose "optional" or "none" to allow logins
# with an unverified e-mail address. In case of "optional", the e-mail
# verification mail is still sent, whereas in case of "none" no e-mail
# verification mails are sent.
ACCOUNT_EMAIL_VERIFICATION = "optional"

# Subject-line prefix to use for email messages sent. By default, the name
# of the current Site (django.contrib.sites) is used.
# ACCOUNT_EMAIL_SUBJECT_PREFIX = '[Site] '

# A string pointing to a custom form class
# (e.g. 'myapp.forms.SignupForm') that is used during signup to ask
# the user for additional input (e.g. newsletter signup, birth
# date). This class should implement a `def signup(self, request, user)`
# method, where user represents the newly signed up user.
# ACCOUNT_SIGNUP_FORM_CLASS = None

# When signing up, let the user type in their password twice to avoid typ-o's.
ACCOUNT_SIGNUP_PASSWORD_VERIFICATION = True

# Enforce uniqueness of e-mail addresses.
ACCOUNT_UNIQUE_EMAIL = True

# A callable (or string of the form 'some.module.callable_name') that takes
# a user as its only argument and returns the display name of the user. The
# default implementation returns user.username.
# ACCOUNT_USER_DISPLAY

# An integer specifying the minimum allowed length of a username.
ACCOUNT_USERNAME_MIN_LENGTH = 8

# The user is required to enter a username when signing up. Note that the
# user will be asked to do so even if ACCOUNT_AUTHENTICATION_METHOD is set
# to email. Set to False when you do not wish to prompt the user to enter a
# username.
ACCOUNT_USERNAME_REQUIRED = True

# render_value parameter as passed to PasswordInput fields.
# ACCOUNT_PASSWORD_INPUT_RENDER_VALUE = False

# Request e-mail address from 3rd party account provider? E.g. using OpenID
# AX, or the Facebook 'email' permission.
SOCIALACCOUNT_QUERY_EMAIL = ACCOUNT_EMAIL_REQUIRED

# Attempt to bypass the signup form by using fields (e.g. username, email)
# retrieved from the social account provider. If a conflict arises due to a
# duplicate e-mail address the signup form will still kick in.
# SOCIALACCOUNT_AUTO_SIGNUP = True

# Enable support for django-avatar. When enabled, the profile image of the
# user is copied locally into django-avatar at signup. Default is
# 'avatar' in settings.INSTALLED_APPS.
# SOCIALACCOUNT_AVATAR_SUPPORT

# Dictionary containing provider specific settings.
SOCIALACCOUNT_PROVIDERS = {
    'orcid': {
        # Base domain of the API. Default value: 'orcid.org', for the production API
        'BASE_DOMAIN':'orcid.org',  # sandbox.orcid.org for the sandbox API
        # Member API or Public API? Default: False (for the public API)
        'MEMBER_API': False,  # for the member API
        'APP': {
            'client_id': 'APP-04ZPI85NJK4Z97OR', # TODO extract to secrets file variable for setup config - this is dev testing only will stop working
            'secret': '9a9e5e9c-414c-4833-b44c-a13c1dbb00e3', # TODO move to environment variable
            'key': ''
        }
    }
}

ACCOUNT_EMAIL_CONFIRMATION_HMAC = True
ACCOUNT_DEFAULT_HTTP_PROTOCOL = "https"
ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 5
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 86400 # 1 day. To strength admin login from being brute forced.
ACCOUNT_LOGOUT_REDIRECT_URL ='/accounts/login/' # where the user lands after logout
LOGIN_REDIRECT_URL = '/' # redirects to profile page by default
ACCOUNT_PRESERVE_USERNAME_CASING = False # reduces the delays in iexact lookups
ACCOUNT_USERNAME_VALIDATORS = None

### End AllAuth Config ###

### Email Config Begin ### #TODO switch to env config
#EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend" # prints to console for dev only TODO: switch with env for smtp for prod
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#DEFAULT_FROM_EMAIL = env("FROM_EMAIL")
DEFAULT_FROM_EMAIL = 'noreply@medborgarforskning.se'
#EMAIL_HOST = env("HOST_EMAIL")
EMAIL_HOST = 'smtp.gu.se'
#EMAIL_HOST_USER = #env("FROM_EMAIL")
#EMAIL_HOST_PASSWORD = #env("EMAIL_HOST_PASSWORD")
EMAIL_PORT = '587'
#EMAIL_USE_TLS = False # True
#EMAIL_USE_SSL = False # depends on provider
#EMAIL_SSL_KEYFILE
#EMAIL_SSL_CERTFILE

#EMAIL_RECIPIENT_LIST = [
#    "jonathan.brier@gu.se",
#]

### Email Config ###

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = '/var/www/arcs_collected_static/static/' # set the location where collectstatic command will place the collected files for serving
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')] # sets where collectstatic command will look for static files to include in collection


# Media files (Users uploaded)
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


# Set the paths to find the local string files used in translation of the site templates - https://docs.djangoproject.com/en/2.2/ref/settings/#locale-paths
# In order of precidence - for robustness and review add the locale path
# 1. LOCALE_PATHS
# 2. locale directory of an app
# 3. django/conf/locale directory as a fallback
LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale')
]



# Set Wagtail Site Name
WAGTAIL_SITE_NAME = 'Pages and Blog of ARCS'

# Enable our CustomUser abstract user for futurproofing and custom auth uses
AUTH_USER_MODEL = 'users.CustomUser'
