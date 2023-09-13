from .base_settings import *

DEGBURG = False

ALLOWED_HOSTS = ["*"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "deptech_db",  # BASE_DIR / "db.sqlite3",
        "USER": "admin@deptech",
        "PASSWORD": "Deptech2023",
        "HOST": "localhost",
        "PORT": "3306",
    }
}
