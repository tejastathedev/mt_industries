from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from products.categories import categories_schema, categories_services


categories_router = APIRouter(prefix="/categories",tags=["Product Categories routes"])

# Create a new product category
@categories_router.post("/create", response_model=categories_schema.CategoriesResponse)
def create_product_category(schema: categories_schema.CreateProductCategories, db: Session = Depends(get_db)):
    return categories_services.create_category(db, schema)


# Retrieve all product categories
@categories_router.get("/getall")
def get_product_categories(db: Session = Depends(get_db)):
    return categories_services.get_categories(db)

# Soft delete a product category by updating its status to 'deleted'
@categories_router.delete("/delete/{category_id}")
def delete_product_category(category_id: int, schema: categories_schema.DeleteProductCategories, db: Session = Depends(get_db)):
    return categories_services.delete_category(db, category_id, schema)

# Update an existing product category
@categories_router.put("/{category_id}", response_model=categories_schema.CategoriesResponse)
def update_product_category(category_id: int, schema: categories_schema.UpdateProductCategories, db: Session = Depends(get_db)):
    return categories_services.update_category(db, category_id, schema)

