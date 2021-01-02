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
