# Содержит основные настройки django проекта
# (конфигурации приложений, шаблонов, middleware...)

from datetime import timedelta
import os
from pathlib import Path
from decouple import config as config_env

# Базовая директория проекта
BASE_DIR = Path(__file__).resolve().parent.parent

# Секретный ключ для безопасности
SECRET_KEY = config_env('SECRET_KEY')

# Режим отладки
DEBUG = config_env('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = config_env('ALLOWED_HOSTS', default='').split(',')

# Список встроенных Django приложений
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# Список сторонних приложений
THIRD_PARTY_APPS = [
    'rest_framework',
    'corsheaders',
    'rest_framework_simplejwt',
]

# Список локальных приложений
LOCAL_APPS = [
    'apps.accounts',
]

# Общий список приложений
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS


# Список middleware для обработки запросов
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Главный URL файл проекта
ROOT_URLCONF = 'config.urls'

# Конфигурация шаблонов Django
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'config.wsgi.application'


# Конфигурация БД
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Валидаторы паролей
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


# Настройка интернациональности
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Europe/Moscow'
USE_I18N = True
USE_TZ = True


# Настройка статических файлов
STATIC_URL = 'static/' # URL статики
STATIC_ROOT = BASE_DIR / 'staticfiles' # Путь для собранных файлов статики

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Настройки Django REST Framework
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',  # Разрешить доступ всем
    ],
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',  # Ограничение запросов для анонимных пользователей
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '100/hour',  # Лимит запросов для анонимных пользователей
    },
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',  # Рендеринг в JSON
    ],
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',  # Парсинг JSON-данных
    ],
}


# # JWT настройки для SimpleJWT
# SIMPLE_JWT = {
#     "ACCESS_TOKEN_LIFETIME": timedelta(minutes=30),  # время жизни access-токена
#     "REFRESH_TOKEN_LIFETIME": timedelta(days=7),     # время жизни refresh-токена
#     "ROTATE_REFRESH_TOKENS": True,                   # при обновлении refresh генерируется новый
#     "BLACKLIST_AFTER_ROTATION": True,                # старый refresh становится недействительным

#     "ALGORITHM": "HS256",
#     "SIGNING_KEY": config_env('SECRET_KEY'),
#     "VERIFYING_KEY": None,

#     "AUTH_HEADER_TYPES": ("Bearer",),                # формат заголовка Authorization
#     "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
#     "USER_ID_FIELD": "id",
#     "USER_ID_CLAIM": "user_id",

#     "TOKEN_TYPE_CLAIM": "token_type",
#     "JTI_CLAIM": "jti",

#     # Дополнительно можно включить сжатие payload
#     "SLIDING_TOKEN_LIFETIME": timedelta(minutes=30),
#     "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=7),
# }


# Настройка CORS для разработки и продакшена
if DEBUG:
    CORS_ALLOW_ALL_ORIGINS = True
else:
    CORS_ALLOWED_ORIGINS = [ # Разрешенные источники
        'http://localhost:5173',
        'http://127.0.0.1:5173',
    ]


# Настройки безопасности
SECURE_BROWSER_XSS_FILTER = True  # Защита от XSS-атак
SECURE_CONTENT_TYPE_NOSNIFF = True  # Запрет MIME-типов
X_FRAME_OPTIONS = 'DENY'  # Защита от кликджекинга


# Настройки логирования
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'INFO',  # Уровень логирования
            'class': 'logging.FileHandler',  # Логирование в файл
            'filename': BASE_DIR / 'debug.log',  # Путь к файлу логов
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],  # Используемый обработчик
            'level': 'INFO',  # Уровень логирования
            'propagate': True,  # Передача логов родительским логгерам
        },
    },
}