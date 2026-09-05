import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

current_file = Path(__file__).resolve()
print(f"Current file: {current_file}")
BASE_DIR = current_file.parent.parent.parent.parent
print(f"Base directory: {BASE_DIR}")
env_path = BASE_DIR / ".env"
print(f".env file path: {env_path}")
print(f"Path exist? {env_path.exists()}")

class Settings:
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = int(os.getenv("DB_PORT", 5432))
    DB_PASS = os.getenv("DB_PASS")
    DB_USER = os.getenv("DB_USER")
    DB_NAME = os.getenv("DB_NAME")

    app_name: str = "FastAPI SHOP"
    debug: bool = True
    cors_origins: list = [
        "http://localhost:5173",
        "http://localhost:3000",
        "http://127.0.0.1:5173",
        "http://127.0.0.1:3000"
    ]
    static_dir: str = 'static'
    images_dir: str = "static/images"

    @property
    def database_url(self) -> str:
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

settings = Settings()