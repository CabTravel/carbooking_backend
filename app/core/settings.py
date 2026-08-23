
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name:str='TravelBook'

    database_hostname:str='localhost'
    database_port: int= 5432
    database_usename:str='postgres'
    database_password:str='1234'
    database_name:str='travelBook'
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379
    REDIS_DB: int = 0


    model_config={
        'env_file':'.env',
        'env_file_encoding':'utf-8',
        'extra':'ignore',
        'case_sensitive':False }

    @property
    def database_url(self) ->str:
        return f"postgresql+asyncpg://{self.database_usename}:{self.database_password}@{self.database_hostname}:{self.database_port}/{self.database_name}";


def get_settings()->Settings:
    return Settings()

    








