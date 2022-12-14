from .base import *

SECRET_KEY = env.str("SECRET_KEY")


DEBUG = env.bool("DJANGO_DEBUG", default=False)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env.str("POSTGRES_DB"),
        'USER': env.str("POSTGRES_USER"),
        'PASSWORD': env.str("POSTGRES_PASSWORD"),
        'HOST': env.str("DB_HOST"),
        'PORT': env.int("DB_PORT")
    }
}