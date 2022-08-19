import os

SECRET_KEY = 'django-insecure-3s6^b$c3+d*@d)_dlu#+mgu6m!68e%ftmo+7pqzrd!py9v!#2y'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_NAME'),
        'USER': os.environ.get('POSTGRES_USER'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': 'db',
        'PORT': 5432,
    }
}