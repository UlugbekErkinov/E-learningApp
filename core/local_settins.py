ALLOWED_HOSTS = ["*"]
DEBUG = True

# Database configuration
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "paycom",
        "USER": "postgres",
        "PASSWORD": "admin",
        "HOST": "localhost",
        "PORT": "5432",
        "ATOMIC_REQUESTS": True,
    }
}


HOST = "http://localhost:8000"

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {"CLIENT_CLASS": "django_redis.client.DefaultClient"},
        "KEY_PREFIX": "elearning",
    },
}
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
