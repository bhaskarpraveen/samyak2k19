import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')o-g4bbm7sh%e$jjrn*$v1f)m^-2l8ok!m+(0@2-^+&1s0*dwz'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG=False

ALLOWED_HOSTS = ['ec2-13-235-200-11.ap-south-1.compute.amazonaws.com','0.0.0.0','klusamyak.in','www.klusamyak.in','localhost','*']

DEFAULT_FROM_EMAIL='your-email'
SENDGRID_API_KEY = os.getenv('SENDGRID_API_KEY')
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD = "Your-password"
EMAIL_PORT = 587
EMAIL_USE_TLS = False

#API_KEY="test_d4044f09402d3410b710105e6dc"
#AUTH_TOKEN="test_c25c6564a1630f1971b8bd10e7e"
# Application definition
API_KEY='YOUR-API-KEY'
AUTH_TOKEN='YOUR-API-TOKEN'
######################
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #'whitenoise.runserver_nostatic',
    'django.contrib.sites', # added for allauth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'stripe',
    'home',
    'newapp',
    'administration',

    'paytm',
    'apitest',
    'products',
    'shopping_cart',
    'crispy_forms',
    'users.apps.UsersConfig',

]
AUTH_USER_MODEL = 'users.CustomUser'
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'cart.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
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

WSGI_APPLICATION = 'cart.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_ROOT =  os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


CRISPY_TEMPLATE_PACK = 'bootstrap4'
# Stripe and Braintree Settings
if DEBUG:
    # test keys
    STRIPE_PUBLISHABLE_KEY =  'YOUR-KEY'
    STRIPE_SECRET_KEY = 'YOUR-KEY'
    BT_ENVIRONMENT='sandbox'
    BT_MERCHANT_ID='YOUR-ID'
    BT_PUBLIC_KEY='YOUR-KEY'
    BT_PRIVATE_KEY='YOUR-KEY'
else:
    # live keys
    STRIPE_PUBLISHABLE_KEY =  'YOUR-KEY'
    STRIPE_SECRET_KEY = 'YOUR-KEY'



# Django AllAuth Settings

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)
USER = " "
SITE_ID = 1

LOGIN_URL = '/profiles/login/'
LOGIN_REDIRECT_URL = '/dashboard/'


PAYTM_MERCHANT_KEY = 'YOUR-KEY'
PAYTM_MERCHANT_ID = 'YOUR-KEY'
HOST_URL = "https://klusamyak.in"
PAYTM_CALLBACK_URL = "/paytm/response/"



PAYTM_WEBSITE = 'WEBSTAGING'

'''
In sandbox enviornment you can use following wallet credentials to login and make payment.
Mobile Number : 7777777777
Password : Paytm12345
OTP: 489871
This test wallet is topped-up to a balance of 7000 Rs. every 5 minutes.
    '''
ACCOUNT_DEFAULT_HTTP_PROTOCOL = "https"
ACCOUNT_LOGOUT_REDIRECT_URL = "/"
