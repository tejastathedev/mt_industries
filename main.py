from fastapi import FastAPI
from database import Base, engine
from orders.router import order_router

app = FastAPI()

# @app.get('/')
# def home_function():
#     return "Server is up !"


app.include_router(order_router)




Base.metadata.create_all(engine)