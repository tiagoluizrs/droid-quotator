from .base import *

DEBUG = False

# Chave secreta preservada por segurança. A mesma deverá ser criada no ambiente de produção apenas.
SECRET_KEY = ''

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# Crie um usuário e senha para adicionar ao banco de dados de produção
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME', 'droid_quotator'),
        'USER': os.getenv('DB_USER', ''),
        'PASSWORD': os.getenv('DB_PASSWORD', ''),
        'HOST': os.getenv('DB_HOST', 'db'),
        'PORT': 5432
    }
}

# JWT Custom configuration
WT_AUTH = {
    'JWT_SECRET_KEY': SECRET_KEY,
    'JWT_ALGORITHM': 'HS256',
    'JWT_VERIFY_EXPIRATION': False,
    'JWT_EXPIRATION_DELTA': None,
}