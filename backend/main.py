# uvicorn main:app --reload
from fastapi import FastAPI

app = FastAPI()


from routes.auth import auth_router
from routes.order import order_router

app.include_router(auth_router)
app.include_router(order_router)