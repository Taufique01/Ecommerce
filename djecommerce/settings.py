import os
from decouple import config



SECRET_KEY = ')=m63ldv543c1q!d7e1mlt)x8a_o1nu*f#x-f+ny#8k(xk7s$q'





BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))





####EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
#Email backend settings for Django
#For less apps
###https://l.facebook.com/l.php?u=https%3A%2F%2Fmyaccount.google.com%2Flesssecureapps%3Fpli%3D1%26fbclid%3DIwAR2CL_EvS0257JaBsqcIGK47_5EHxSaw1ZQMk2h9-R3laFTvsA8j9LiUNOw&h=AT3bkopboKv9FC-NRSloYitPDjXJuutczWQYT8kAt6GnU9F4CT9k35W_T75UX-DW0neaCl0YuO36C38uvfX492HiRRNDrJCcpSADz4c57njDKJSNRoW4O0Nq0l7QaQ
####
# Email backend settings for Django
EMAIL_BACKEND ='django.core.mail.backends.smtp.EmailBackend' #  'django.core.mail.backends.console.EmailBackend'# 
EMAIL_HOST = 'smtp.zoho.com'
##put yours email
EMAIL_HOST_USER = 'info@novonil.com'
##put your password
EMAIL_HOST_PASSWORD = 'WMmTFvxL93YN'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

DEFAULT_FROM_EMAIL='TAUFIQUE_HATBAJAR<info@novonil.com>'



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}



INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'crispy_forms',
    'django_countries',

    'core'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'djecommerce.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
          BASE_DIR + '/templates/',
         ],
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

WSGI_APPLICATION = 'djecommerce.wsgi.application'

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static_in_env')]
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media_root')

# Auth#### ALL AUTH

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend'
)
SITE_ID = 1
LOGIN_REDIRECT_URL = '/'
ACCOUNT_EMAIL_REQUIRED=True
ACCOUNT_EMAIL_VERIFICATION='mandatory'
# CRISPY FORMS

CRISPY_TEMPLATE_PACK = 'bootstrap4'





STRIPE_SECRET_KEY=''
DEBUG=True
