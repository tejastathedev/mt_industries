from pydantic import BaseModel

# Create Product Weight Units
class CreateProductWeightUnit(BaseModel):
    name: str
    created_by : int

# Update Product Weight Units
class UpdateProductWeightUnit(BaseModel):
    name: str
    updated_by : int


# Delete Product Weight Units
class DeleteProductWeightUnit(BaseModel):
    deleted_by : int
    deletion_date: str

class weightUnitResponse(BaseModel):
    id: int
    name: str
    created_by: int

    class Config:
        orm_mode = True

        
