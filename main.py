from fastapi import FastAPI
from database import Base, engine
from users.router import auth_router
from utils.exception_handler import ExceptionHandler
from cron_jobs.scheduler import init_scheduler


app = FastAPI()
app.include_router(auth_router)

@app.get('/')
def home_function():
    return "Server is up !"

# call exception handler for raising all the exception from one file/location
ExceptionHandler(app)  


# Start scheduler
scheduler = init_scheduler()

Base.metadata.create_all(engine)