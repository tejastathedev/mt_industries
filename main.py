from fastapi import FastAPI, HTTPException, status
from database import Base, engine
from utils.exception_handler import ExceptionHandler
app = FastAPI()

@app.get('/')
def home_function():
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Data not found")
    return "Server is up !"

# call exception handler for raising all the exception from one file/location
ExceptionHandler(app)  


Base.metadata.create_all(engine)