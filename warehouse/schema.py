from pydantic import BaseModel


class WarehouseSchema(BaseModel):
    company_id: int
    latitude: float
    longitude: float
    address: str
    warehouse_name: str
    warehouse_manager: str
    details: str
