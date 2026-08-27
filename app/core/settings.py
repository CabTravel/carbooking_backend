
from pydantic_settings import BaseSettings
from urllib.parse import quote_plus

class Settings(BaseSettings):
    app_name:str='TravelBook'

    database_hostname:str
    database_port: int
    database_username:str
    database_password:str
    database_name:str
    redis_host: str 
    redis_port: int
    redis_db: int
    # s3 cucket config
    r2_account_id=str
    r2_access_key_id=str
    r2_secret_access_key=str
    r2_bucket_name= str
    r2_public_url=str
    



    model_config={
        'env_file':'.envremote',
        'env_file_encoding':'utf-8',
        'extra':'ignore',
        'case_sensitive':False }



    @property
    def database_url(self) -> str:
        return (
            f"postgresql+asyncpg://"
            f"{quote_plus(self.database_username)}:"
            f"{quote_plus(self.database_password)}@"
            f"{self.database_hostname}:"
            f"{self.database_port}/"
            f"{self.database_name}?ssl=require"
        )

    @property
    def database_url(self) -> str:
        return (
            f"postgresql+asyncpg://"
            f"{quote_plus(self.database_username)}:"
            f"{quote_plus(self.database_password)}@"
            f"{self.database_hostname}:"
            f"{self.database_port}/"
            f"{self.database_name}?ssl=require"
        )



def get_settings()->Settings:
    return Settings()

    








