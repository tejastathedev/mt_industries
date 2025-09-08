from fastapi import FastAPI
from database import Base, engine
from users.router import user_router
from auth.router import auth_router
from company.router import company_router
from extras.router import extra_router
from warehouse.router import warehouse_router
from utils.exception_handler import ExceptionHandler
# from cron_jobs.scheduler import init_scheduler
from products.models import *
from products.units.product_units_routers import product_units_router
from products.weightUnits.product_weightunit_routers import weightunit_router
from products.categories.categories_router import categories_router
from products.dimensionUnits.dimension_routers import dimension_router


app = FastAPI()
app.include_router(auth_router)
app.include_router(user_router)
app.include_router(company_router)
app.include_router(extra_router)
app.include_router(warehouse_router)


# Product routers
# Include product units router
app.include_router(product_units_router)

# Include product weight units router
app.include_router(weightunit_router)

# Include product categories router
app.include_router(categories_router)

# Include product dimension units router
app.include_router(dimension_router)

Base.metadata.create_all(engine)

@app.get('/')
def home_function():
    return "Server is up !"




8000
# call exception handler for raising all the exception from one file/location
ExceptionHandler(app)


# Start scheduler
# scheduler = init_scheduler()
<<<<<<< HEAD
=======
@app.on_event("startup")
def start_scheduler():
    init_scheduler()

Base.metadata.create_all(engine)
>>>>>>> 4adc65a67a0fb1c71747d6bc2d95dd606f5c9e34
