from pydantic import BaseSettings


class Settings(BaseSettings):
    DB_HOST: str
    DB_USER = str
    DB_PASSWORD = str
    DB_HOSTNAME = str
    DB_PORT = int
    DB_NAME = str

    class Config:
        env_file = "../.env"


settings = Settings()