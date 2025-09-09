from fastapi import FastAPI
from database import Base, engine
from users.router import user_router
from ucompany.routers import company_routers
from userscope.routers import userscope_router
from wearhouse.routers import wearhouse_router
# from auth.router import auth_router
from utils.exception_handler import ExceptionHandler
# from cron_jobs.scheduler import init_scheduler



app = FastAPI()
# app.include_router(auth_router)
app.include_router(userscope_router)
app.include_router(company_routers)
app.include_router(wearhouse_router)
app.include_router(user_router,tags=['user'])

@app.get('/')
def home_function():
    return "Server is up !"

# call exception handler for raising all the exception from one file/location
# ExceptionHandler(app)  


# Start scheduler
# scheduler = init_scheduler()

Base.metadata.create_all(engine)