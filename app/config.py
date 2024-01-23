"""
hold config settings draw from env file @todo lru cache
"""
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """
    settings class, hold config drawn from env file
    """
    app_name: str
    db_engine: str
    db_host: str
    db_user: str
    db_password: str

    model_config = SettingsConfigDict(env_file=".env")
    