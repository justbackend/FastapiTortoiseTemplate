from app.config import settings

# DATABASE_URL = os.getenv("DATABASE_URL", "sqlite://db.sqlite3")
TORTOISE_ORM = {
    "connections": {
        "default": settings.postgres_url_tortoise,
    },
    "apps": {
        "models": {
            "models": ["app.user.models"],
            "default_connection": "default",
        },
    },
}
