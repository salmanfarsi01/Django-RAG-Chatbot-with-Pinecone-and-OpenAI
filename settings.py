# chatbot_project/settings.py

import os
from pathlib import Path
from dotenv import load_dotenv  # Import the load_dotenv function

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Load environment variables from .env file
load_dotenv(os.path.join(BASE_DIR, '.env')) # Specify the path to .env

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/stable/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# Get the SECRET_KEY from the environment variable
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True # For development, you can set this to True. For production, set it in your .env file.

ALLOWED_HOSTS = []

# ... rest of the settings.py file