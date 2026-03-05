from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    #criptografia de senha
    SECRET_KEY: str
    #access tokens 
    ALGORITHM: str
    ACESS_TOKEN_EXPIRE_MINUTES: int

    class Config:
        env_file = ".env"

settings = Settings()