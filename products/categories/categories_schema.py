from pydantic import BaseModel


# Create Product Categories
class CreateProductCategories(BaseModel):
    name : str
    description : str
    created_by  : int
    company_id : int

# Update Product Categories
class UpdateProductCategories(BaseModel):
    name : str
    description : str
    updated_by  : int


# Delete Product Categories
class DeleteProductCategories(BaseModel):
    deleted_by : int
    deletion_date: str

class CategoriesResponse(BaseModel):
    id: int
    name: str
    description: str
    created_by: int
    company_id: int

    class Config:
        orm_mode = True
