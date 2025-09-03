import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

class Settings:
    STATUS_ENUM = os.getenv("STATUS_ENUM", "active,deleted").split(",")
    ORDER_STATUS_ENUM = os.getenv("ORDER_STATUS_ENUM", "pending,dispatched,delivered,returned,rejected,cancelled").split(",")

settings = Settings()
