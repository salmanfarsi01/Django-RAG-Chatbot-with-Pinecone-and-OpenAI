"""
WSGI config for chatbot_project project.
It exposes the WSGI callable as a module-level variable named ``application``.
For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
from dotenv import load_dotenv  # <-- ADD THIS LINE

from django.core.wsgi import get_wsgi_application

load_dotenv()  # <-- AND ADD THIS LINE

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatbot_project.settings')

application = get_wsgi_application()