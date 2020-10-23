# This is all boilerplate, don't touch this file for now!
import sys
import os
from django.conf import settings
from django.core.management import execute_from_command_line

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

settings.configure(
    DEBUG=True,
    ROOT_URLCONF='urls',
    STATIC_URL='static/',
    STATIC_ROOT=os.path.join(BASE_DIR, 'static'),
    ALLOWED_HOSTS= ['tranquil-caverns-16220.herokuapp.com', '127.0.0.1'],
    INSTALLED_APPS=[
        'django.contrib.staticfiles',
    ],
    TEMPLATES=[{
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
    }],
)

execute_from_command_line(sys.argv)
