from fastapi import APIRouter, Depends, HTTPException
from datetime import timedelta

#acesso ao bd
from sqlalchemy.orm import Session
from backend.models.models import Usuario
from backend.core.dependencies import pegar_sessao

#segurança
from backend.security.criptografia import bcrypt_context
from backend.security.authenticator import autenticar_usuario
from backend.security.jwt_handler import criar_token, verificar_token
from fastapi.security import OAuth2PasswordRequestForm

from backend.schemas.schemas import UsuaruioSchema, LoginSchema

auth_router = APIRouter(prefix="/auth")


@auth_router.get("/")
async def home():
    return{"autentucado": "ola"}

#rota para criar conta
@auth_router.post("/criar_conta")
async def criar_conta(usuario_schemas: UsuaruioSchema, session = Depends(pegar_sessao)):
    usuario = session.query(Usuario).filter(Usuario.email==usuario_schemas.email).first()
    if usuario:
        # ja existe usuario com esse email
        raise HTTPException(status_code=400, detail="E-mail já cadastrado")
    else:
        senha_criptografada = bcrypt_context.hash(usuario_schemas.senha)
        novo_usuario = Usuario(usuario_schemas.nome, usuario_schemas.email, senha_criptografada, usuario_schemas.ativo)
        session.add(novo_usuario)
        session.commit()
        return{"mensagem": "usuario cadastrado com sucesso"}
    
#rota de login
@auth_router.post("/login")
async def login(login_schema: LoginSchema,session: Session = Depends(pegar_sessao)):
    usuario = autenticar_usuario(login_schema.email, login_schema.senha, session)
    if not usuario:
        raise HTTPException(status_code=401, detail="Usuário não encontrado")
    else:
        access_token = criar_token(usuario.id)
        refresh_token = criar_token(usuario.id, duracao_token=timedelta(days=7))
        return{
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "Bearer"
        }
    
#rota de login admin
@auth_router.post("/admin/login")
async def admin_login(login_schema: LoginSchema,session: Session = Depends(pegar_sessao)):
    usuario = autenticar_usuario(login_schema.email, login_schema.senha, session)
    if not usuario:
        raise HTTPException(status_code=401, detail="Usuário não encontrado")
    if not usuario.admin:
        raise HTTPException(status_code=403, detail="Acesso restrito a administradores")
    else:
        access_token = criar_token(usuario.id)
        refresh_token = criar_token(usuario.id, duracao_token=timedelta(days=7))
        return{
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "Bearer"
        }
    
@auth_router.post("/login-form")
async def login_form(dados_form: OAuth2PasswordRequestForm = Depends(), session: Session = Depends(pegar_sessao)):
    usuario = autenticar_usuario(dados_form.username, dados_form.password, session)
    if not usuario:
        raise HTTPException(status_code=401, detail="Usuário não encontrado")
    else:
        access_token = criar_token(usuario.id)
        return{
            "access_token": access_token,
            "token_type": "Bearer"
        }
    
@auth_router.get("/refresh")
async def use_refresh_token(usuario: Usuario = Depends(verificar_token)):
    access_token = criar_token(usuario.id)
    return{
            "access_token": access_token,
            "token_type": "Bearer"
        }