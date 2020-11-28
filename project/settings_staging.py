from .settings import *


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG will be either True or False. True = '1' False = '0'
DEBUG = bool(int(os.getenv('DEBUG', str(int(False)))))

ALLOWED_HOSTS = ['.herokuapp.com', 'cocktail-api.jasonhubbard.dev']

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# SECURE_SSL_REDIRECT = True
