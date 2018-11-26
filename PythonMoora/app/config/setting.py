import os, django

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

SECRET_KEY = '-24xiv-slr_^o^n72e+in^(iufnsp9v@!9j^gb4ec28l#@!p6i'
DEBUG = True
ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '10.10.1.88',
]

PROJECT_APPS = [
    'orm',
    'management.nilai_akademik',
    'management.hasiltes',
    'management.siswa',
    'management.kelas',
    'management.plomba',
    'management.karakter',
    'management.hasil_akhir',
    'management.bobot',
    'management.data_siswa',
    'login',
    'soal.soalbiologi',
    'soal.soalfisika',
    'soal.soalkimia',
    'soal.soalmatematika',
    'soal.daftar_olimpiade',
    'library',
    'data_user',
    'soal.tesolimpiade',


    
]

REQUIRED_APPS = [
    'material',
    'material.frontend',
    'material.admin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'widget_tweaks',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

INSTALLED_APPS = REQUIRED_APPS + PROJECT_APPS

ROOT_URLCONF = 'app.urls'
WSGI_APPLICATION = 'app.wsgi.application'

from app.config.auth import *
from app.config.database import *
from app.config.international import *
from app.config.static import *
from app.config.media import *
django.setup()
from app.config.template import *

