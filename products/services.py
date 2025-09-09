from sqlalchemy.orm import Session
from fastapi import HTTPException
from products import schemas,models
import datetime,config

def create_product(db:Session, products:schemas.RegisterProduct):
    db_product=db.query(models.Products).filter(
        models.Products.name==products.name,
        models.Products.weight==products.weight,
        models.Products.dimensions==products.dimensions
        ).first()
    if db_product:
        raise HTTPException(status_code=404,detail="Product Already Registered in Database.!")
    
    new_product=models.Products(
        name=products.name,
        description=products.description,
        img=products.img,
        sku=products.sku,
        weight=products.weight,
        dimensions=products.dimensions,
        brand_name=products.brand_name,

        cost_price=products.cost_price,
        market_price=products.market_price,
        selling_price=products.selling_price,
        initial_stock=products.initial_stock,

        created_by=products.created_by,
        updated_by=None,
        deleted_by=None,

        creation_date=datetime.date.today(),
        updation_date=None,
        deletion_date=None,
 
        dimension_unit_id=products.dimension_unit_id,
        category_id=products.category_id,
        weight_unit_id=products.weight_unit_id,
        unit_id=products.unit_id,
        company_id=products.company_id,

        status=config.settings.STATUS_ENUM[0]
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

def update_product(db:Session,products:schemas.UpdateProduct,product_id:int,product_name:str):
    db_product=db.query(models.Products).filter(
        models.Products.id==product_id,
        models.Products.name==product_name,
        ).first()
    if not db_product:
        raise HTTPException(status_code=404,detail="Product Not Found.!")
    

    db_product.name=products.name
    db_product.description=products.description
    db_product.img=products.img
    db_product.sku=products.sku
    db_product.weight=products.weight
    db_product.dimensions=products.dimensions
    db_product.brand_name=products.brand_name

    db_product.cost_price=products.cost_price
    db_product.market_price=products.market_price
    db_product.selling_price=products.selling_price
    db_product.initial_stock=products.initial_stock
    
    db_product.updated_by=products.updated_by
    db_product.created_by=models.Products.created_by
    db_product.updation_date=datetime.date.today()
    db_product.deletion_date=None
 
    db_product.dimension_unit_id=products.dimension_unit_id
    db_product.category_id=products.category_id
    db_product.weight_unit_id=products.weight_unit_id
    db_product.unit_id=products.unit_id
    db_product.company_id=products.company_id

    db_product.status=config.settings.STATUS_ENUM[0]
    
    db.commit()
    db.refresh(db_product)
    return db_product

def delete_product(db:Session,product_id:int,product_name:str,deleted_by:int):
    db_product=db.query(models.Products).filter(
        models.Products.id==product_id,
        models.Products.name==product_name
        ).first()
    if not db_product:
        raise HTTPException(status_code=404,detail="Product Not Found.!")
    if db_product.status == config.settings.STATUS_ENUM[1]:
        raise HTTPException(status_code=404,detail="Data Already Deleted.!")
    db_product.deleted_by=deleted_by
    db_product.status=config.settings.STATUS_ENUM[1]
    db_product.deletion_date=datetime.date.today()

    db.commit()
    db.refresh(db_product)

    # data={
    #     "product_id":db_product.id,
    #     "product_name":db_product.name,
    #     "product_brand":db_product.brand_name,
    #     "product_status":db_product.status
    # }
    return db_product

def show_all_products(db:Session,company_id:int):
    db_user = db.query(models.Products).filter(
    models.Products.company_id == company_id
    ).all()
    if not db_user:
        raise HTTPException(status_code=404, detail="No products found for this company!")
    return db_user
