from fastapi import FastAPI
from database import Base, engine
from users.router import auth_router

app = FastAPI()
app.include_router(auth_router)

@app.get('/')
def home_function():
    return "Server is up !"

Base.metadata.create_all(engine)