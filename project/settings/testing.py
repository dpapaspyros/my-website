# pylint: disable=wildcard-import,unused-wildcard-import
from .base import *

# Load DB credentials from CI config
if os.environ.get('DATABASE_POSTGRESQL_USERNAME', ''):
    DATABASES['default']['NAME'] = os.environ.get('DATABASE_POSTGRESQL_NAME', '')
    DATABASES['default']['USER'] = os.environ.get('DATABASE_POSTGRESQL_USERNAME', '')
    DATABASES['default']['PASSWORD'] = os.environ.get('DATABASE_POSTGRESQL_PASSWORD', '')
    DATABASES['default']['PORT'] = '5432'
