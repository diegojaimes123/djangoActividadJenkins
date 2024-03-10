"""
Django settings for app_reservas project.

Generated by 'django-admin startproject' using Django 4.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import dj_database_url
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-r$*0qbor^@fewg$+o1^c^0b8owf5$*ajj@q)kw$dufh3!qaech'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Configuración de ALLOWED_HOSTS: Lista de hosts permitidos para el servidor.
# Asegúrate de incluir aquí los hosts desde los cuales esperas solicitudes.
# En entornos de desarrollo comunes, se incluyen localhost, 127.0.0.1 y 10.0.2.2.
# En producción, agrega el nombre de host de tu dominio.
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '10.0.2.2']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',  # Registro de Django Rest Framework
    'corsheaders',
    'coreapi',  # Registro de Django Cors Headers
    'api',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'app_reservas.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'app_reservas.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
# Conexión a la base de datos
DATABASES = {
    'default': dj_database_url.config(
        default='postgres://usersena:j6LTWFak6z94POivkic7OM59ZzLnUMJM@dpg-cnitnlvsc6pc73d2kgeg-a.frankfurt-postgres.render.com/reserva_db_6f09',
        conn_max_age=600
    )
}



# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.AllowAny",
    ],
}

# Configuración de CORS_ALLOWED_ORIGINS: Lista de orígenes permitidos para solicitudes CORS.
# En esta configuración se definen los dominios desde los cuales se permitirán solicitudes CORS.
# Asegúrate de incluir aquí los dominios que corresponden al Front-End y Back-End de tu aplicación.
# Esto es esencial para permitir solicitudes desde diferentes dominios, como el Front-End y Back-End,
# y evitar problemas de política de mismo origen (Same-Origin Policy).
CORS_ALLOWED_ORIGINS = (
    "http://localhost:65500",  # Dominio del componente Front-End
    "http://localhost:8000",  # Dominio del componente Back-End
)

# Dominio del componente Front-End
CSRF_TRUSTED_ORIGINS = ["http://localhost:65500"]

APPEND_SLASH = False
