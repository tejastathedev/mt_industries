import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

class Settings:
    STATUS_ENUM = os.getenv("STATUS_ENUM", "active,deleted").split(",")
    ORDER_STATUS_ENUM = os.getenv("ORDER_STATUS_ENUM", "pending,dispatched,delivered,returned,rejected,cancelled").split(",")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY","")
    JWT_ALGORITHM = os.getenv("JWT_ALGORITHM","")
    ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES","")
    REFRESH_TOKEN_EXPIRE_DAYS = os.getenv("REFRESH_TOKEN_EXPIRE_DAYS","")

settings = Settings()
