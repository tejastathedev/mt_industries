from fastapi import FastAPI
from database import Base, engine
from users.router import user_router
from auth.router import auth_router
from company.router import company_router
from extras.router import extra_router
from warehouse.router import warehouse_router
from utils.exception_handler import ExceptionHandler
from cron_jobs.scheduler import init_scheduler

from products.router import productrouter
from products.ProductHistory.router import producthistoryrouter


app = FastAPI()
# app.include_router(auth_router)
# app.include_router(user_router)
app.include_router(productrouter)
app.include_router(producthistoryrouter)
app.include_router(auth_router)
app.include_router(user_router)
app.include_router(company_router)
app.include_router(extra_router)
app.include_router(warehouse_router)


@app.get('/')
def home_function():
    return "Server is up !"

# call exception handler for raising all the exception from one file/location
# ExceptionHandler(app)  


# Start scheduler
# scheduler = init_scheduler()
@app.on_event("startup")
def start_scheduler():
    init_scheduler()

Base.metadata.create_all(engine)