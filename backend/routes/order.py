from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from backend.schemas.schemas import PedidoSchema, ItemPedidoSchema, ResponsePedidoSchema
from backend.models.models import Pedido, Usuario, ItemPedido, Product
from backend.security.jwt_handler import verificar_token
from backend.core.dependencies import pegar_sessao

order_router = APIRouter(prefix="/pedidos", tags=["pedidos"], dependencies=[Depends(verificar_token)])

@order_router.get("/")
async def pedidos():
    return {"order": "ok"}

@order_router.post("/pedido")
async def criar_pedido(pedido_schema: PedidoSchema, session: Session = Depends(pegar_sessao)):
    
    novo_pedido = Pedido(usuario=pedido_schema.usuario)
    session.add(novo_pedido)
    session.flush()  # gera o id do pedido sem commitar ainda

    for item in pedido_schema.itens:
        produto = session.query(Product).filter(Product.id == item.product_id).first()
        if not produto:
            raise HTTPException(status_code=404, detail=f"Produto {item.product_id} não encontrado")

        novo_item = ItemPedido(
            quantidade=item.quantidade,
            product_id=item.product_id,
            product_size_id=item.product_size_id,
            pedido_id=novo_pedido.id,
            preco_unitario=produto.price
        )
        session.add(novo_item)

    session.flush()
    novo_pedido.calcular_preco()
    session.commit()

    return {
        "mensagem": "Pedido criado com sucesso",
        "id_pedido": novo_pedido.id,
        "preco_total": novo_pedido.preco
    }

@order_router.post("/pedido/remover-item/{id_item_pedido}")
async def remover_item_pedido(id_item_pedido:int,
                                session: Session = Depends(pegar_sessao),
                                usuario: Usuario = Depends(verificar_token)):
    
    item_pedido = session.query(ItemPedido).filter(ItemPedido.id==id_item_pedido).first()
    pedido = session.query(Pedido).filter(Pedido.id==item_pedido.pedido).first()
    if not item_pedido:
        raise HTTPException(status_code=400, detail="item do pedido não existente")
    if not usuario.admin and usuario.id != item_pedido.pedido.usuario:
        raise HTTPException(status_code=401, detail="Você não tem autorização")
    session.delete(item_pedido)
    pedido.calcular_preco()
    session.commit()
    return{
        "mensagem": "item removido com sucesso",
        "preço predido": len(pedido.itens),
        "pedido": pedido
    }

@order_router.get("/listar")
async def listar_pedidos(session: Session = Depends(pegar_sessao), usuario: Usuario = Depends(verificar_token)):
    if not usuario.admin:
        raise HTTPException(status_code=401, detail="Voce não tem autorização")
    else:
        pedidos = session.query(Pedido).all()
        return {
            "pedidos": pedidos
        }
    
@order_router.post("/pedido/cancelar/{id_pedido}")
async def cancelar_pedido(id_pedido: int, session: Session = Depends(pegar_sessao), usuario: Usuario = Depends(verificar_token)):
    pedido = session.query(Pedido).filter(Pedido.id==id_pedido).first()
    if not pedido: 
        raise HTTPException(status_code=400, detail="pedido não encontrado")
    if not usuario.admin and usuario.id != pedido.usuario:
        raise HTTPException(status_code=401, detail="Voce não tem autorização")
    pedido.status = "CANCELADO"
    session.commit()
    return{
        "mensagem": f"pedido numero: {pedido.id} cancelado com sucesso",
        "pedido": pedido
    }

# finalizar pedido 
@order_router.post("/pedido/finalizar/{id_pedido}")
async def finalizar_pedido(id_pedido: int, session: Session = Depends(pegar_sessao), usuario: Usuario = Depends(verificar_token)):
    pedido = session.query(Pedido).filter(Pedido.id==id_pedido).first()
    if not pedido: 
        raise HTTPException(status_code=400, detail="pedido não encontrado")
    if not usuario.admin and usuario.id != pedido.usuario:
        raise HTTPException(status_code=401, detail="Voce não tem autorização")
    pedido.status = "FINALIZADO"
    session.commit()
    return{
        "mensagem": f"pedido numero: {pedido.id} FINALIZADO com sucesso",
        "pedido": pedido
    }

# vizualizar 1 pedido
@order_router.get("/pedido/{id_pedido}")
async def vizualizar_pedido(id_pedido: int, session: Session = Depends(pegar_sessao), usuario: Usuario = Depends(verificar_token)):
    pedido = session.query(Pedido).filter(Pedido.id==id_pedido).first()
    if not pedido:
        raise HTTPException(status_code=400, detail="pedido não encontrado")
    if not pedido: 
        raise HTTPException(status_code=400, detail="pedido não encontrado")
    if not usuario.admin and usuario.id != pedido.usuario:
        raise HTTPException(status_code=401, detail="Voce não tem autorização")
    return{
        "quantidade_itens_pedido": len(pedido.itens),
        "pedido": pedido
    }


# vizualizar todos os pedidos de 1 usuario
@order_router.get("/listar/pedidos-usuario", response_model=List[ResponsePedidoSchema])
async def listar_pedidos(session: Session = Depends(pegar_sessao), usuario: Usuario = Depends(verificar_token)):
        pedidos = session.query(Pedido).filter(Pedido.usuario==usuario.id).all()
        return  pedidos