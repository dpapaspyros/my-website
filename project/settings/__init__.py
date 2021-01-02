import os
import sys

ENVIRONMENT = os.environ.get('ENVIRONMENT', 'DEV').upper()


if ENVIRONMENT == 'PRODUCTION':
    from .production import *
elif 'test' in sys.argv:
    from .testing import *
else:
    from .dev import *
