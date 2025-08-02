from pydantic_settings import BaseSettings

class Configuration(BaseSettings):
    api_url: str
