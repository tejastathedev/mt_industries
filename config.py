import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()


class Settings:
    STATUS_ENUM = os.getenv("STATUS_ENUM", "active,deleted").split(",")
    ORDER_PAYMENT_TYPE = os.getenv("STATUS_ENUM", "COD,UPI").split(",")
    ORDER_STATUS_ENUM = os.getenv(
        "ORDER_STATUS_ENUM", "pending,dispatched,delivered,returned,rejected,cancelled"
    ).split(",")

    DATA_ADDED_SUCCESSFULLY = os.getenv(
        "DATA_ADDED_SUCCESSFULLY", "Data added successfully"
    )
    DATA_NOT_FOUND = os.getenv("DATA_NOT_FOUND", "No data found")
    DATA_ALREADY_EXISTS = os.getenv("DATA_ALREADY_EXISTS", "Data already exists")
    DATA_UPDATED_SUCCESSFULLY = os.getenv(
        "DATA_UPDATED_SUCCESSFULLY", "Data updated successfully"
    )
    DATABASE_ERROR = os.getenv("DATABASE_ERROR", "Database error: {error}")
    UNEXPECTED_ERROR = os.getenv("UNEXPECTED_ERROR", "Unexpected error: {error}")
    DATA_VALIDATION_ERROR = os.getenv(
        "DATA_VALIDATION_ERROR", "Data validation error: {error}"
    )
    DUPLICATE_DATA_ERROR = os.getenv(
        "DUPLICATE_DATA_ERROR", "Duplicate data error: {error}"
    )

    ORDER_STATUS_ENUM = os.getenv("ORDER_STATUS_ENUM", "pending,dispatched,delivered,returned,rejected,cancelled").split(",")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY","")
    JWT_ALGORITHM = os.getenv("JWT_ALGORITHM","")
    ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES","")
    REFRESH_TOKEN_EXPIRE_DAYS = os.getenv("REFRESH_TOKEN_EXPIRE_DAYS","")

settings = Settings()
