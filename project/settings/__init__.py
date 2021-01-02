import os
import sys

ENVIRONMENT = os.environ.get('ENVIRONMENT', 'DEV').upper()


if ENVIRONMENT == 'PRODUCTION':
    from .production import *
else:
    from .dev import *
