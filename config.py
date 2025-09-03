import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

class Settings:
    STATUS_ENUM = os.getenv("STATUS_ENUM", "active,deleted").split(",")
    ORDER_STATUS_ENUM = os.getenv("ORDER_STATUS_ENUM", "pending,dispatched,delivered,returned,rejected,cancelled").split(",")

    DATA_ADDED_SUCCESSFULLY = os.getenv("DATA_ADDED_SUCCESSFULLY","DATA_ADDED_SUCCESSFULLY")
    DATA_NOT_FOUND = os.getenv("DATA_NOT_FOUND","DATA_NOT_FOUND")
    DATA_ALREADY_EXISTS = os.getenv("DATA_ALREADY_EXISTS","DATA_ALREADY_EXISTS")
    DATA_UPDATED_SUCCESSFULLY = os.getenv("DATA_UPDATED_SUCCESSFULLY","DATA_UPDATED_SUCCESSFULLY")
    DATABASE_ERROR = os.getenv("DATABASE_ERROR","DATABASE_ERROR")
    UNEXPECTED_ERROR = os.getenv("UNEXPECTED_ERROR","UNEXPECTED_ERROR")
    DATA_VALIDATION_ERROR = os.getenv("DATA_VALIDATION_ERROR","DATA_VALIDATION_ERROR")
    DUPLICATE_DATA_ERROR = os.getenv("DUPLICATE_DATA_ERROR","DUPLICATE_DATA_ERROR")

settings = Settings()
