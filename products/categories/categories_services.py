from ..models import Categories
from ..categories.categories_schema import CreateProductCategories, UpdateProductCategories, DeleteProductCategories, CategoriesResponse
from datetime import datetime
from fastapi import HTTPException
from config import settings


# Service functions for product categories
# Create a new product category

def create_category(db, schema: CreateProductCategories):
    # Check if a category with the same name already exists and is not deleted
    existing_category = db.query(Categories).filter(
        Categories.name == schema.name,
        Categories.status != settings.STATUS_ENUM[1]  # Exclude 'deleted' categories
    ).first()

    # If it exists, raise an HTTP 400 error
    if existing_category:
        raise HTTPException(
            status_code=400,
            detail="Category with this name already exists."
        )
    # If it doesn't exist, create a new category
    new_category = Categories(
        name=schema.name,
        description=schema.description,
        created_by=schema.created_by,
        company_id=schema.company_id,
        status=settings.STATUS_ENUM[0],  # 'active' is the first status in the list
        creation_date=datetime.now()
    )

    db.add(new_category)
    db.commit()
    db.refresh(new_category)  # ← necessary to get the auto-generated ID

    return new_category  # This matches response_model=CategoriesResponse



# Retrieve all product categories
def get_categories(db):
    categories=db.query(Categories).filter(Categories.status != settings.STATUS_ENUM[1]).all()  # Exclude 'deleted' categories
    if not categories:
        return []
    return categories


# Soft delete a product category by updating its status to 'deleted'
def delete_category(db, category_id: int, schema: DeleteProductCategories):
    category = db.query(Categories).filter(Categories.id == category_id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    category.deleted_by = schema.deleted_by
    category.deletion_date = datetime.now()
    category.status = settings.STATUS_ENUM[1]  #'deleted' is the second status in the list
    db.commit()
    return "Category deleted successfully"

# Update an existing product category
def update_category(db, category_id :int, schema: UpdateProductCategories):
    category = db.query(Categories).filter(Categories.id == category_id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    
    # Check if a different category with the same name already exists and is not deleted
    existing_category = db.query(Categories).filter(
        Categories.name == schema.name,
        Categories.id != category_id,
        Categories.status != settings.STATUS_ENUM[1]  # Exclude 'deleted' categories
    ).first()

    if existing_category:
        raise HTTPException(
            status_code=400,
            detail="Another category with this name already exists."
        )

    category.name = schema.name
    category.description = schema.description
    category.updated_by = schema.updated_by
    category.last_update_date = datetime.now()
    
    db.commit()
    db.refresh(category)  # ← to get the updated data

    return category  # This matches response_model=CategoriesResponse
