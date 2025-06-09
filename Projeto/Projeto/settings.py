from pathlib import Path
import os  # adicionado para usar os.path.join

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# ------------------------------
# CONFIGURAÇÕES DE PRODUÇÃO
# ------------------------------

# Segurança
SECRET_KEY = 'django-insecure-_n-f!o_kk5&&mqn))@^3yd4!ow-1!(oap#5gx+$!%qclm(bh)6'

DEBUG = False  # produção NUNCA deve usar debug True

ALLOWED_HOSTS = ['malufnb.pythonanywhere.com']


# ------------------------------
# APLICAÇÕES
# ------------------------------

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'credenciamento',
    'aplicacao',
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

ROOT_URLCONF = 'Projeto.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Projeto.wsgi.application'


# ------------------------------
# BANCO DE DADOS
# ------------------------------

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# ------------------------------
# VALIDAÇÃO DE SENHAS
# ------------------------------

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# ------------------------------
# LOCALIZAÇÃO
# ------------------------------

LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Recife'

USE_I18N = True
USE_TZ = True


# ------------------------------
# ARQUIVOS ESTÁTICOS
# ------------------------------

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # para uso com collectstatic

# opcionalmente:
# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# ------------------------------
# OUTRAS CONFIGURAÇÕES
# ------------------------------

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Redirecionamento padrão para login se não autenticado
LOGIN_URL = '/'
LOGIN_REDIRECT_URL = '/aplicacao/perfil/'
