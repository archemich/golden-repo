from pydantic_settings import BaseSettings

class Configuration(BaseSettings):
    db_url: str
