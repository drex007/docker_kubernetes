"""
WSGI config for docker_kub project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
import pathlib #We are trying to use this [path lib to import the path of our .env file
from django.core.wsgi import get_wsgi_application
from dotenv import load_dotenv
load_dotenv()


CURRENT_DIR = pathlib.Path(__file__).resolve().parent #Path => Parent of our file 
BASE_DIR = CURRENT_DIR.parent #Access ing the base dir of the project
ENV_FILE_PATH = BASE_DIR / ".env" #Env path 
env = os.getenv(str(ENV_FILE_PATH))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'docker_kub.settings')

application = get_wsgi_application()
