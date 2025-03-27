import os
from pathlib import Path

from dotenv import load_dotenv
from pydantic import BaseModel

ROOT = Path(__file__).parent.parent

load_dotenv()


class DatabaseSettings(BaseModel):
    path: str = os.environ.get('DB_PATH').format(ROOT)
    echo: bool = bool(int(os.environ.get('DB_ECHO')))


class Settings(BaseModel):
    api_path: str = os.environ.get('API_PATH')
    tron_api_key: str = os.environ.get('TRON_API_KEY')
    db: DatabaseSettings = DatabaseSettings()


settings = Settings()
