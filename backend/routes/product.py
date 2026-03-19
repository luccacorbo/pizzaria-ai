from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session


product_router = APIRouter(prefix="/produtos", tags=["produtos"])


@product_router.post("/criar-produtos")
async def criar_produtos():
    return