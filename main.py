from fastapi import FastAPI
from database import Base, engine

app = FastAPI()

@app.get('/')
def home_function():
    return "Server is up !"

Base.metadata.create_all(engine)