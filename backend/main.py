# uvicorn backend.main:app --reload
from fastapi import FastAPI

app = FastAPI()


from backend.routes.auth import auth_router
from backend.routes.order import order_router
from backend.routes.product import product_router


app.include_router(auth_router)
app.include_router(order_router)
app.include_router(product_router)
