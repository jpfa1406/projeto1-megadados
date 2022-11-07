from sqlalchemy.orm import Session

from . import models, schemas

def get_products(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Product).offset(skip).limit(limit).all()

def get_product(db: Session, product_id: int):
    return db.query(models.Product).filter(models.Product.id == product_id).first()

def create_product(db: Session, product: schemas.ProductCreate):
    db_product = models.Product(name=product.name, 
                                description=product.description, 
                                price=product.price)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def update_product(db: Session, product: schemas.ProductCreate, product_id: int):
    db.query(models.Product).filter(models.Product.id == product_id).update({
        'name': product.name,
        'description': product.description,
        'price': product.price
    })
    db.commit()

def delete_product(db: Session, product_id: int):
    product = get_product(db, product_id)
    db.delete(product)
    db.commit()
