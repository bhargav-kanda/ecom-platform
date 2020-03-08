"""
Django settings for zapyle_new project.

Generated by 'django-admin startproject' using Django 1.8.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from mongoengine import connect


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*&009=kr-0dpqy^@16xf05ak!ev^gh8scxk@z)4b)6vqp5@%w%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []
SESSION_COOKIE_NAME = 'zsd'


# Application definition
from django.utils.crypto import get_random_string

INSTALLED_APPS = (
    'django.contrib.admindocs',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.postgres',
    "push_notifications",
    "djcelery",
    "dbbackup",
    'rest_framework',
    'zap_apps.zapuser',
    'zap_apps.account',
    'zap_apps.address',
    'zap_apps.zap_catalogue',
    'zap_apps.marketing',
    'zap_apps.zap_upload',
    'zap_apps.onboarding',
    'zap_apps.zap_admin',
    'zap_apps.discover',
    'zap_apps.payment',
    'zap_apps.cart',
    'zap_apps.coupon',
    'zap_apps.order',
    'zap_apps.referral',
    'zap_apps.zap_notification',
    'zap_apps.logistics',
    'zap_apps.offer',
    'zap_apps.zap_search',
    'zap_apps.zap_analytics',
    'zap_apps.extra_modules',
    'djrill',
    'frontend',
    'zap_apps.blog',
    'rest_framework_mongoengine',
    'django_extensions',
    'zap_apps.drip',
    'django_ses',
    'seacucumber',
    'django.contrib.humanize',
    'storages',
)

MIDDLEWARE_CLASSES = (
    # 'zap_apps.account.zap_middleware.ProfileMiddleware',
    'zap_apps.account.zap_middleware.DisableCSRFOnDebug',
    'zap_apps.account.zap_middleware.SettingPlatformHeader',
    # 'zap_apps.account.zap_middleware.DisableCSRFForCitrus',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    # 'zap_apps.account.zap_middleware.CheckSuperUser',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    #middleware for html minification
    # 'htmlmin.middleware.HtmlMinifyMiddleware',
    # 'htmlmin.middleware.MarkRequestMiddleware',

)
HTML_MINIFY = True

ROOT_URLCONF = 'zapyle_new.urls'
# EMAIL_BACKEND = "djrill.mail.backends.djrill.DjrillBackend"
# MANDRILL_API_KEY = "39BHLWt2NAcJKD3NDmrMlA"


# MANDRILL_API_KEY = "iBkrW2RHlFC7WpQtZqz4Dg"


#EMAIL_BACKEND = "zap_apps.zap_notification.djsb.DjsbBackend"
EMAIL_BACKEND = 'seacucumber.backend.SESBackend'
AWS_SES_REGION_NAME = 'us-west-2'
AWS_SES_REGION_ENDPOINT = 'email.us-west-2.amazonaws.com'
AWS_ACCESS_KEY_ID = 'AKIAJD423ECNNXK3LMDA'
AWS_SECRET_ACCESS_KEY = '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'
CELERY_DISABLE_RATE_LIMITS = False
# Rate limit to three outgoing SES emails a second.
CUCUMBER_RATE_LIMIT = 10


SENDIN_BLUE_ACCESS_KEY = 'gxdMGXhj5tfBw1rk'

DEFAULT_FROM_EMAIL = "support@zapyle.com"
FROM_EMAIL = 'support@zapyle.com'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(os.path.dirname(BASE_DIR), "zap_templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'zap_apps.zap_catalogue.views.WebsiteHeaderProducts',
            ],
        },
    },
]

WSGI_APPLICATION = 'zapyle_new.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'zapyle_db',
        'USER': 'zapadmin',
        'PASSWORD': 'zapy!e1234',
        'HOST': 'localhost',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'zapyle_db',
#         'USER': 'zapadmin',
#         'PASSWORD': 'zapy!e1234',
#         'HOST': 'zapyle-dev.cijbxbnbcn1g.us-west-1.rds.amazonaws.com',
#         'PORT': '5432'
#     }
# }

DBBACKUP_STORAGE = 'dbbackup.storage.filesystem_storage'
DBBACKUP_STORAGE_OPTIONS = {'location': BASE_DIR+'/backup'}
DBBACKUP_CLEANUP_KEEP = 1
DBBACKUP_CLEANUP_KEEP_MEDIA = 1


JUSPAY_ENV = 'sandbox'
JUSPAY_API_KEY = '398208417EF64442830F6E89B009EFD0'
# JUSPAY_ENV = 'production'
# JUSPAY_API_KEY = 'B9609E37792544B083C40F86BC4BB26A'

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

INSTAGRAM_CLIENT_ID = "6d7335f42651482f890e8d4ea58d3370"
INSTAGRAM_CLIENT_SECRET = "799369f441d948969e86532c39289b5d"
FB_CLIENT_ID = "1602519030013216"


STATIC_URL = '/zapstatic/'
# STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'


MEDIA_URL = '/zapmedia/'
AUTHENTICATION_BACKENDS = (
    'zap_apps.account.zapauth.FBAuthBackend',
    'zap_apps.account.zapauth.InstgramAuthBackend',
    'zap_apps.account.zapauth.EmailAuthBackend',
    'django.contrib.auth.backends.ModelBackend',
    )

REST_FRAMEWORK = {
    'PAGE_SIZE': 15,
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        # 'rest_framework.renderers.BrowsableAPIRenderer',
        # 'rest_framework.renderers.TemplateHTMLRenderer',
    ],
   'DEFAULT_AUTHENTICATION_CLASSES': (
       'rest_framework.authentication.BasicAuthentication',
       'rest_framework.authentication.SessionAuthentication',
    ),
   'EXCEPTION_HANDLER': 'zap_apps.account.zapauth.zap_exception_handler',
   # 'DEFAULT_PARSER_CLASSES': (
    #    'rest_framework.parsers.JSONParser',
    #)
}
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

ADMINS = (
    ('Ram', 'ram@zapyle.com'),
    ('Shafi', 'shafi@zapyle.com'),
    )

#celery
# CELERY_DEFAULT_QUEUE = 'zap_queue'
CELERY_RESULT_BACKEND='djcelery.backends.database:DatabaseBackend'
CELERY_USE = True

PLACEHOLDER_IMG_URL = 'frontend/placeholder.png'
BRAND_TAG_LIMIT = 20
BRAND_LIMIT = 25
CATALOGUE_SELLERVIEW_LINE_ITEM_COUNT = 4
CATALOGUE_PERPAGE = 28
NOTIFICATION_PERPAGE = 20
SELLERVIEW_PAGE_LINE_COUNT = 10
SELLER_CLOSET_PERPAGE = 10
SHIPPING_CHARGE_PRICE_LIMIT = 1500
SHIPPING_CHARGE = 0
SELECTED_BRANDS = ['Gucci', 'Sabyasachi', 'Louis Vuitton', 'Tory Burch', 'BCBG Maxazria']
#ENCRYPTIONKEY
ENCKEY = "ZaXcu6wp"
PUSHBOT_ID = "55d3021b17795969478b4569"
PUSHBOT_SECRET = "b66ee0e7be3d827c85e3343c3d42f96a"
# PUSHBOT_ID = "56a20cb017795945648b4567" #mee
# PUSHBOT_SECRET = "2938d33877f87e3eb1d768b38eba8dd8"
# PUSHBOT_ID = "56cc0c131779590a408b4567"
# PUSHBOT_SECRET = "d96fb77b4b031933c7d50d9e5d4dba34"
#PAYMENT
# MERCHANT_ACCESS_KEY = "GS3K0UGZOG8WQ6KQIG61"
# MERCHANT_SECRET_KEY = "d3a491a58cd44dee4149141888936f7d5df082d9"
# CITRUS_RETURN_URL = "http://localhost:9000/payment/zappaymentreturn/"
# CITRUS_WEBSITE_RETURN_URL = "http://localhost:9000/payment/zappaymentreturn/website/"
HOME_FOLDER = os.path.dirname(BASE_DIR) 

PUSH_NOTIFICATIONS_SETTINGS = {
       "GCM_API_KEY": "AIzaSyDVvrcs1ezmWRX_jiaz5flXwIHoos3lOn8",
       # "GCM_API_KEY": "AIzaSyDHOeH8pyK61d4TBTn9J3rXTwi3_556_UQ",
       "APNS_CERTIFICATE": HOME_FOLDER+'/pushcert_dev.pem',
}
OTP_DISABLE = True
#LOGISTICS

TORNADO_URL = 'http://localhost:8888/odanrot'


from email_notifications import *
from zapsms import *
#DELHIVERY_KEY
DELHIVERY_SERVICE = True
DELHIVERY_BASE_URL = 'https://test.delhivery.com'
DELHIVERY_API_KEY = 'b5944330ef5e20dd66ae9aacfaf589a49ff28171'
DELHIVERY_PICKUP_NAME = 'ZAPYLE - DFS'


#ARAMEX
ARAMEX_SERVICE = True
ARAMEX_BASE_URL = 'https://ws.dev.aramex.net'

ARAMEX_LABEL_URL = '/shippingapi/shipping/service_1_0.svc/json/PrintLabel'
ARAMEX_CREATE_SHIPMENT_URL = '/shippingapi/shipping/service_1_0.svc/json/CreateShipments'
ARAMEX_CREATE_PICKUP_URL = '/shippingapi/shipping/service_1_0.svc/json/CreatePickup'
ARAMEX_UPDATE_URL = '/ShippingAPI.V2/Tracking/Service_1_0.svc/json/TrackShipments'

ARAMEX_USERNAME = "testingapi@aramex.com"
ARAMEX_PASSWORD = "R123456789$r"
ARAMEX_VERSION = "v1"
ARAMEX_ACCOUNT_NUMBER = "BLRTST001"
ARAMEX_ACCOUNT_PIN = "113634"
ARAMEX_ACCOUNT_ENTITY = "BLR"
ARAMEX_ACCOUNT_COUNTRY_CODE = "IN"
ARAMEX_SOURCE = 24


#NOTIFICATIONS
PUSH_NOTIFICATION_ENABLE = True
EMAIL_NOTIFICATION_ENABLE = True
SMS_NOTIFICATION_ENABLE = False
EASTER_REFERRAL = True
ZAPCASH_REFERRAL = 200

#PARCELLED
PARCELLED_SERVICE = False
PARCELLED_API_KEY = '_Cl6nADizsWuKHWOl-34bg'
PARCELLED_BASE_URL = 'http://staging-pa.parcelled.in/api/v1/'
PARCEL_CHECK_ENABLED = True

#MVC ZAPCASH SETTINGS
MVC_ISSUE_URL = 'https://sandboxcoupons.citruspay.com/cms_api.asmx/IssueCoupons'
MVC_REDEEM_URL = 'https://sandboxcoupons.citruspay.com/cms_api.asmx/RedeemCampaign'
MVC_ROLL_BACK_URL = 'https://sandboxcoupons.citruspay.com/cms_api.asmx/RollbackCampaign'
MVC_BALANCE_URL = 'https://sandboxcoupons.citruspay.com/cms_api.asmx/FetchCampaignBalance'
MVC_PARTNER_ID = 'za61q0w33q'
MVC_PASSWORD = 'GS3K0UGZOG8WQ6KQIG61'
MVC_MERCHANT_ID = 'za61q0w33q'

#CITRUS
# MERCHANT_ACCESS_KEY = "GS3K0UGZOG8WQ6KQIG61"
# MERCHANT_SECRET_KEY = "d3a491a58cd44dee4149141888936f7d5df082d9"
# MERCHANT_VANITY_URL = 'za61q0w33q'
# CITRUS_SIGNIN_ID = 'za61q0w33q-signin'
# CITRUS_SIGNIN_CLIENT_SECRET = 'fa772fe4dca0e25f0161d98e240c5759'
# CITRUS_SIGNUP_ID = 'za61q0w33q-signup'
# CITRUS_SIGNUP_CLIENT_SECRET =  'bb77a0bc677bc69233ccbd3f9610417a'
# CITRUS_JS_SIGNIN_ID = 'za61q0w33q-JS-signin'
# CITRUS_JS_SIGNUP_ID = 'dc49e0196e0e9af4b45249a87599b539'
# CITRUS_CASH_REFUND_URL = 'https://sandboxadmin.citruspay.com/service/v2/prerefund/refund'
# CITRUS_CASH_PAY_URL = 'https://sandboxadmin.citruspay.com/service/v2/prepayment/prepaid_pay'
# CITRUS_CASH_BALANCE_URL = 'https://sandboxadmin.citruspay.com/service/v2/prepayment/balance'
# CITRUS_ENQUIRY_URL = 'https://sandboxadmin.citruspay.com/api/v2/txn/enquiry/'

# CITRUS_GET_SAVED_CARD_URL = 'https://sandboxadmin.citruspay.com/service/v2/profile/me/payment'
# CITRUS_SIGNIN_TOKEN_URL = 'https://sandboxadmin.citruspay.com/oauth/token'
# CITRUS_SIGNUP_TOKEN_URL = 'https://sandboxadmin.citruspay.com/oauth/token'
# CITRUS_SIGNUP_URL = 'https://sandboxadmin.citruspay.com/service/um/link/user/extended'
# CITRUS_ENV = 'DEBUG'


# CITRUS_MRK_AUTH_URL = "https://splitpaysbox.citruspay.com/marketplace/auth/"
# CITRUS_MRK_SELLER_URL = 'https://splitpaysbox.citruspay.com/marketplace/seller/'
# CITRUS_MRK_SPLIT_URL = 'https://splitpaysbox.citruspay.com/marketplace/split/'
# CITRUS_MRK_RELEASE_URL = 'https://splitpaysbox.citruspay.com/marketplace/funds/release/'

# CITRUS_REFUND_URL = 'https://sandboxadmin.citruspay.com/api/v2/txn/refund'

#citrus production settings
MERCHANT_ACCESS_KEY = "R05H4Q7GB1XX3SWQ98IF"
MERCHANT_SECRET_KEY = "751652eeac5c9a98a1203d04a1cadd9edb956d80"
MERCHANT_VANITY_URL = 'cqoos6l2u2'
CITRUS_SIGNIN_ID = 'cqoos6l2u2-signin'
CITRUS_SIGNIN_CLIENT_SECRET = 'afee8d44e739705c7d7c347d0c3d89d4'
CITRUS_SIGNUP_ID = 'cqoos6l2u2-signup'
CITRUS_SIGNUP_CLIENT_SECRET =  '2268ae0137ab1fadb1f83235cf23847a'
CITRUS_JS_SIGNIN_ID = 'cqoos6l2u2-JS-signin'
CITRUS_JS_SIGNUP_ID = '112b13d6297c4a9a476fb833b7b12b93'
CITRUS_CASH_REFUND_URL = 'https://admin.citruspay.com/service/v2/prerefund/refund'
CITRUS_CASH_PAY_URL = 'https://admin.citruspay.com/service/v2/prepayment/prepaid_pay'
CITRUS_CASH_BALANCE_URL = 'https://admin.citruspay.com/service/v2/prepayment/balance'
CITRUS_ENQUIRY_URL = 'https://admin.citruspay.com/api/v2/txn/enquiry/'

CITRUS_GET_SAVED_CARD_URL = 'https://admin.citruspay.com/service/v2/profile/me/payment'
CITRUS_SIGNIN_TOKEN_URL = 'https://admin.citruspay.com/oauth/token'
CITRUS_SIGNUP_TOKEN_URL = 'https://admin.citruspay.com/oauth/token'
CITRUS_SIGNUP_URL = 'https://admin.citruspay.com/service/um/link/user/extended'
CITRUS_ENV = 'PRODUCTION'
DEFAULT_HTTP_PROTOCOL = 'http'


CITRUS_MRK_AUTH_URL = "https://splitpay.citruspay.com/marketplace/auth/"
CITRUS_MRK_SELLER_URL = 'https://splitpay.citruspay.com/marketplace/seller/'
CITRUS_MRK_SPLIT_URL = 'https://splitpay.citruspay.com/marketplace/split/'
CITRUS_MRK_RELEASE_URL = 'https://splitpay.citruspay.com/marketplace/funds/release/'

CITRUS_REFUND_URL = 'https://admin.citruspay.com/api/v2/txn/refund'
#LOGISTICS


LOGISTICS_DOMAIN = 'www.zapyle.com'
LOGISTICS_IMG_DOMAIN = 'zapmob.cloudapp.net/media'

MONGO_DB_TRACKER = True
ITEM_INCREASE_AFTER_PAYMENT_FAIL_TIME = 60 * 10

class Struct:
    def __init__(self, **entries):
        for key, value in entries.iteritems():
            v2 = (Struct(**value) if isinstance(value, dict) else value) 
            self.__dict__[key] = self.__dict__[key] = v2
import json
with open(BASE_DIR+'/settings/custom_errors.json') as err:
    ZAPERROR = Struct(**json.loads(err.read()))
ERROR_KEYS = ['invalid', 'max_length', 'min_length', 'null', 'blank', 'required','does_not_exist','incorrect_type']
ZAP_ENV_VERSION = get_random_string(10)
# CELERY_RESULT_BACKEND='djcelery.backends.database:DatabaseBackend'

WKHTMLTOPDF_PATH = '/usr/local/bin/wkhtmltopdf'

#APP_VIRALITY
APPVIRALITY_ENABLE = True
API_URL = 'https://api.appvirality.com'
APP_KEY = '80ea0f13b9f8485d8f2fa5de0135d8b5'
PRIVATE_KEY = 'zapy!e1234'
REFERRER_AMOUNT = 100
FRIEND_AMOUNT = 100

#MIXPANEL
MIXPANEL_TOKEN = "cdcedd9556628c0ac79f0d2a70a363c2"

#GUEST
SHOW_GUEST = True

MIN_PURCHASE = 100


#SLACK
SLACK_INCOMING_WEBHOOK_URL = "https://hooks.slack.com/services/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"


BULK_NOTIFICTAION_QUEUE = 'test_push_queue'
BULK_NOTIFICTAION_RESP_QUEUE = 'test_push_response_queue'

AWS_QUERYSTRING_AUTH = False

GRAPH_MODELS = {
  'all_applications': True,
  'group_models': True,
}

EXOTEL_SID = "zapyle1"
EXOTEL_TOKEN = "a4aa70dfc9427c8460f92451428c70b0cc12ea71"
EXOTEL_URL = "https://"+EXOTEL_SID+":"+EXOTEL_TOKEN+"@twilix.exotel.in/v1/Accounts/"+EXOTEL_SID+"/Sms/send"
EXOTEL_FROM = "08033172908"

ELASTIC_URL = 'https://search-zapylesearch-oh745tarex4gbmbmndo7ek6inq.us-west-1.es.amazonaws.com/develop/products/'

ZAPYLE_BILL_EMAIL = ['shafi@zapyle.com']