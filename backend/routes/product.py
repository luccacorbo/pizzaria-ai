from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.schemas.schemas import ProdutoSchema
from backend.models.models import Product, Usuario
from backend.security.jwt_handler import verificar_token
from backend.core.dependencies import pegar_sessao


product_router = APIRouter(prefix="/produtos", tags=["produtos"], dependencies=[Depends(verificar_token)])


@product_router.post("/criar-produtos")
async def criar_produto(produto_schema: ProdutoSchema,
                         session:Session = Depends(pegar_sessao),
                         usuario: Usuario = Depends(verificar_token)):
    if not usuario.admin:
        raise HTTPException(status_code=401, detail="Você não tem autorização")

    novo_produto = Product(
    name=produto_schema.nome,
    description=produto_schema.descricao,
    price=produto_schema.preco,
    active=produto_schema.ativo,
    category_id=produto_schema.category_id)

    session.add(novo_produto)
    session.commit()
    return{"mensagem": f"produto criado com sucesso. ID do pedido {novo_produto.id}"}
