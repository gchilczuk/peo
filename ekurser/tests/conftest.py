import pytest

@pytest.fixture()
def django_db_setup(settings):
    settings.DATABASES['default'] = {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'kursy',
        'USER': 'pomaster',
        'PASSWORD': 'pomasterpass',
        'HOST': 'poaws.cbx5ewzaapbo.us-east-1.rds.amazonaws.com',
        'PORT': '5432'
    }