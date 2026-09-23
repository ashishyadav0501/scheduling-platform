from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application configuration, loaded from environment variables / .env."""

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )

    app_name: str = "Scheduling Platform API"
    app_env: str = "development"
    log_level: str = "INFO"
    database_url: str
    db_echo: bool = False


@lru_cache
def get_settings() -> Settings:
    return Settings()