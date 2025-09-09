from pydantic import BaseModel
from datetime import datetime


# Create Dimension Units
class CreateDimensionUnits(BaseModel):
    name: str
    description: str
    created_by: int
    company_id: int

# Update Dimension Units
class UpdateDimensionUnits(BaseModel):
    name : str
    description : str
    updated_by  : int
    updation_date: datetime


# Delete Dimension Units
class DeleteDimensionUnits(BaseModel):
    deleted_by : int
    deletion_date: datetime

class DimensionUnitsResponse(BaseModel):
    id: int
    name: str
    description: str
    created_by: int
    company_id: int

    class Config:
        orm_mode = True