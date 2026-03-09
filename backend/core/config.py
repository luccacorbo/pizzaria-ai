from pydantic_settings import BaseSettings, SettingsConfigDict
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

class Settings(BaseSettings):
    #criptografia de senha
    SECRET_KEY: str
    #access tokens 
    ALGORITHM: str
    ACESS_TOKEN_EXPIRE_MINUTES: int
    #db
    DATABASE_URL: str

    model_config = SettingsConfigDict(env_file=f"{BASE_DIR}/.env")
  

settings = Settings()