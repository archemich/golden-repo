from pydantic_settings import BaseSettings

class Configuration(BaseSettings):
    db_url: str
    rabbitmq_url: str
    payments_queue_name: str
