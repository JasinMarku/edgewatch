from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    database_url: str = Field(
        default="postgresql+asyncpg://postgres:postgres@localhost:5432/edgewatch",
        alias="DATABASE_URL",
    )
    odds_api_key: str | None = Field(default=None, alias="ODDS_API_KEY")
    openai_api_key: str | None = Field(default=None, alias="OPENAI_API_KEY")
    edge_threshold: int = Field(default=7, ge=0, alias="EDGE_THRESHOLD")

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_prefix="",
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
