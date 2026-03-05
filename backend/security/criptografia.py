from passlib.context import CryptContext
from core.config import settings
from fastapi.security import OAuth2PasswordBearer


SECRET_KEY = settings.SECRET_KEY

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated ="auto")
oauth2_schema = OAuth2PasswordBearer(tokenUrl="auth/login-form")