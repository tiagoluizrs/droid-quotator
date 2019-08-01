from .base import *

DEBUG = True

# Crie a secret key para seu ambiente de desenvolvimento
SECRET_KEY = ''

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "memory:",
    }
}
EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"

# JWT Custom configuration
WT_AUTH = {
    'JWT_SECRET_KEY': SECRET_KEY,
    'JWT_ALGORITHM': 'HS256',
    'JWT_VERIFY_EXPIRATION': False,
    'JWT_EXPIRATION_DELTA': None,
}