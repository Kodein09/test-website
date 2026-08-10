import os

from dotenv import load_dotenv

load_dotenv("../../../.env")

class Settings:
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = int(os.getenv("DB_PORT", 5432))
    DB_PASS = os.getenv("DB_PASS")
    DB_USER = os.getenv("DB_USER")
    DB_NAME = os.getenv("DB_NAME")

    @property
    def database_url(self) -> str:
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

settings = Settings()