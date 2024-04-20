from pathlib import Path
import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy.engine.url import URL

load_dotenv()

DIR = Path(__file__).absolute().parent.parent.parent
BOT_DIR = Path(__file__).absolute().parent.parent
LOCALES_DIR = f'{BOT_DIR}/locales'
MEDIA_DIR = f'{DIR}/mediafiles'


class EnvBaseSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        extra='ignore'
    )


class BotSettings(BaseSettings):
    BOT_TOKEN: str
    SUPPORT_URL: str | None = None
    RATE_LIMIT: int | float = 0.5  # for throttling control
    REVIEWS_HUB_URL: str | None = None


class DBSettings(EnvBaseSettings):
    DB_HOST: str = os.getenv('DB_HOST', 'postgres')
    DB_PORT: int = os.getenv('DB_PORT', 5432)
    DB_USER: str = os.getenv('DB_USER', 'postgres')
    DB_PASS: str | None = os.getenv('DB_PASS', None)
    DB_NAME: str = os.getenv('DB_NAME', 'postgres')

    @property
    def database_url(self) -> URL | str:
        if self.DB_PASS:
            return f'postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'
        return f'postgresql+asyncpg://{self.DB_USER}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'

    @property
    def database_url_psycopg2(self) -> str:
        if self.DB_PASS:
            return f'postgresql://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'
        return f'postgresql://{self.DB_USER}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'


class CacheSettings(EnvBaseSettings):
    REDIS_HOST: str = os.getenv('REDIS_HOST', 'redis')
    REDIS_PORT: int = os.getenv('REDIS_PORT', 6379)
    REDIS_PASS: str | None = os.getenv('REDIS_PASS', None)

    # REDIS_DATABASE: int = 1
    # REDIS_USERNAME: int | None = None
    # REDIS_TTL_STATE: int | None = None
    # REDIS_TTL_DATA: int | None = None

    @property
    def redis_url(self) -> str:
        if self.REDIS_PASS:
            return f'redis://{self.REDIS_PASS}@{self.REDIS_HOST}:{self.REDIS_PORT}/0'
        return f'redis://{self.REDIS_HOST}:{self.REDIS_PORT}/0'


class Settings(BotSettings, DBSettings, CacheSettings):
    DEBUG: bool = False


settings = Settings()
