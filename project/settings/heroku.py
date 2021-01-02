# pylint: disable=wildcard-import,unused-wildcard-import
from .base import *

import dj_database_url

DATABASES = {
    'default': dj_database_url.config()
}
DATABASES['default']['CONN_MAX_AGE'] = 500

ALLOWED_HOSTS = ['*']

# Whitenoise
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
WHITENOISE_MANIFEST_STRICT = False

# SSl settings
# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True
