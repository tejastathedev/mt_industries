from fastapi import FastAPI
from database import Base, engine
from utils.exception_handler import ExceptionHandler
app = FastAPI()

@app.get('/')
def home_function():
    return "Server is up !"

# call exception handler for raising all the exception from one file/location
ExceptionHandler(app)  


Base.metadata.create_all(engine)