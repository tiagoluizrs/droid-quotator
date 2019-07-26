from .base import *

DEBUG = True

# Crie a secret key para seu ambiente de desenvolvimento
SECRET_KEY = ''

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# Crie um usuário e senha para adicionar ao banco de dados de desenvolvimento
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('DB_NAME', 'droid_quotator'),
        'USER': os.getenv('DB_USER', ''),
        'PASSWORD': os.getenv('DB_PASSWORD', ''),
        'HOST': os.getenv('DB_HOST', 'localhost'),
        'PORT': '3306'
    }
}