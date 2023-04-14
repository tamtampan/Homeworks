"""Config Module"""

from pydantic import BaseSettings


class Settings(BaseSettings):
    """Base settings"""

    DB_HOST: str
    DB_HOSTNAME: str
    DB_PORT: int
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str
    USER_SECRET: str
    ALGORITHM: str

    DB_NAME_TEST: str
    USE_TEST_DB: bool

    class Config:
        """Config class"""

        env_file = "./.env"


settings = Settings()
