from fastapi import FastAPI
from database import Base, engine
from users.router import user_router
from auth.router import auth_router
from utils.exception_handler import ExceptionHandler
# from cron_jobs.scheduler import init_scheduler
from products.models import *
from products.units.product_units_routers import product_units_router


app = FastAPI()
app.include_router(auth_router)
app.include_router(user_router)

# Include product units router
app.include_router(product_units_router)

Base.metadata.create_all(engine)

@app.get('/')
def home_function():
    return "Server is up !"





# call exception handler for raising all the exception from one file/location
ExceptionHandler(app)


# Start scheduler
# scheduler = init_scheduler()
