from security.criptografia import bcrypt_context
from models.models import Usuario

def autenticar_usuario(email, senha, session):
    usuario = session.query(Usuario).filter(Usuario.email==email).first()
    if not usuario: 
        return False
    elif not bcrypt_context.verify(senha, usuario.senha):
        return False
    return usuario