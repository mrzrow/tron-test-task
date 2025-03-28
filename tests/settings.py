import os

from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()


class TestDatabaseSettings(BaseModel):
    path: str = os.environ.get('TEST_DB_PATH')
    echo: bool = bool(int(os.environ.get('DB_ECHO')))


class TestSettings(BaseModel):
    api_path: str = os.environ.get('API_PATH')
    tron_api_key: str = os.environ.get('TRON_API_KEY')
    db: TestDatabaseSettings = TestDatabaseSettings()


test_settings = TestSettings()
