from pydantic import BaseModel


class CreateProductWeightUnit(BaseModel):
    id: int
    name: str
    created_by : int

# Update Product Units
class UpdateProductWeightUnit(BaseModel):
    name: str
    updated_by : int


# Delete Product Units
class DeleteProductWeightUnit(BaseModel):
    deleted_by : int
    deletion_date: str

class weightUnitResponse(BaseModel):
    id: int
    name: str
    created_by: int
