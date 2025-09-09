from pydantic import BaseModel
from enum import Enum



# Product Units Schema

# Create Product Units
class CreateProductUnits(BaseModel):
    name: str
    created_by : int

# Update Product Units
class UpdateProductUnits(BaseModel):
    name: str
    updated_by : int


# Delete Product Units
class DeleteProductUnits(BaseModel):
    deleted_by : int
    deletion_date: str

class UnitResponse(BaseModel):
    id: int
    name: str
    created_by: int

