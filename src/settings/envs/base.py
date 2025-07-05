from pydantic_settings import BaseSettings, SettingsConfigDict

from src.settings.envs.configs.db import DBSettings
from src.settings.configs.rabbitmq import RabbitMQSettings
from src.settings.configs.redis import RedisSettings


class Settings(
    BaseSettings,
    DBSettings,
    RabbitMQSettings,
    RedisSettings,
):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    DB_SCHEMA: str
    PREFIX: str
    TOKEN: str
    TEST_TOKEN: str
    DEBUG: bool
    ADMIN_IDS: list[int]


settings = Settings()
