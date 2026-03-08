from fastapi import Depends, HTTPException
from datetime import datetime, timedelta, timezone
from sqlalchemy.orm import Session
from jose import jwt, JWTError
from backend.core.config import settings
from backend.core.dependencies import pegar_sessao
from backend.models.models import Usuario
from backend.security.criptografia import oauth2_schema


def criar_token(id_usuario, duracao_token=timedelta(minutes=settings.ACESS_TOKEN_EXPIRE_MINUTES)):
    data_expiracao = datetime.now(timezone.utc) + duracao_token
    dic_info = {"sub": str(id_usuario), "exp": data_expiracao}
    jwt_codificado = jwt.encode(dic_info, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

    return jwt_codificado

def verificar_token(token: str = Depends(oauth2_schema), session: Session = Depends(pegar_sessao)):

    try:
        dic_info = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        id_usuario = int(dic_info.get("sub"))
    except JWTError:
        raise HTTPException(status_code=401, detail="Acesso Negado")
    
    usuario = session.query(Usuario).filter(Usuario.id==id_usuario).first()
    if not usuario:
        raise HTTPException(status_code=401, detail="Acesso Inválido")
    return usuario
