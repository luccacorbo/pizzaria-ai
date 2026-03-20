from sqlalchemy import create_engine, Column, String, Integer, Boolean,DECIMAL, Float, ForeignKey 
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy_utils.types import ChoiceType
from backend.core.config import settings


db = create_engine(settings.DATABASE_URL)

Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String, nullable=False)
    email = Column("email", String, nullable=False, unique=True)
    senha = Column("senha", String, nullable=False)
    ativo = Column("ativo", Boolean)
    admin = Column("admin", Boolean, default=False)

    def __init__(self, nome, email, senha, ativo=True, admin=False):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo
        self.admin = admin

class Pedido(Base):
    __tablename__ = "pedidos"


    id = Column("id", Integer, primary_key=True, autoincrement=True)
    status = Column("status", String) #pendente, cancelado, finalizado 
    usuario = Column("usuario", ForeignKey("usuarios.id"))
    preco = Column("preco", Float)
    itens = relationship("ItemPedido", cascade="all, delete")

    def __init__(self, usuario, status="PENDENTE", preco=0):
        self.usuario = usuario
        self.status = status
        self.preco = preco
    
    def calcular_preco(self):
        self.preco = sum(item.preco_unitario * item.quantidade for item in self.itens)

class ItemPedido(Base):
    __tablename__ = "itens_pedido"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    quantidade = Column("quantidade", Integer) 
    preco_unitario = Column("preco_unitario", Float)

    pedido_id = Column(Integer, ForeignKey("pedidos.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
    product_size_id = Column(Integer, ForeignKey("product_sizes.id"))

#categoria de produtos
class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    active = Column(Boolean, default=True)


#tabela para produtos do site(criavel para admins)
class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)
    price = Column(Float)
    active = Column(Boolean, default=True)

    category_id = Column(Integer, ForeignKey("categories.id"))
    category = relationship("Category", backref="products")

    sizes = relationship("ProductSize", back_populates="product")

class ProductSize(Base):
    __tablename__ = "product_sizes"

    id = Column(Integer, primary_key=True)
    size = Column(String)  # Pequena, Média, Grande

    product_id = Column(Integer, ForeignKey("products.id"))
    product = relationship("Product", back_populates="sizes")