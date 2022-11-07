from sqlalchemy.orm import Session

from . import models, schemas

def get_products(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Product).offset(skip).limit(limit).all()

def get_product(db: Session, product_id: int):
    return db.query(models.Product).filter(models.Product.id == product_id).first()

def create_product(db: Session, product: schemas.ProductCreate):
    db_product = models.Product(name=product.name, 
                                description=product.description, 
                                price=product.price,
                                quantity = product.quantity)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def update_product(db: Session, product: schemas.ProductCreate, product_id: int):
    db.query(models.Product).filter(models.Product.id == product_id).update({
        'name': product.name,
        'description': product.description,
        'price': product.price,
        'quantity': product.quantity
    })
    db.commit()

def delete_product(db: Session, product_id: int):
    product = get_product(db, product_id)
    db.delete(product)
    db.commit()

def get_movimentacoes(db: Session, skip: int = 0, limit: int = 0):
    return db.query(models.Movimentacao).offset(skip).limit(limit).all()

def get_movimentacao(db: Session, movimentacao_id: int):
    return db.query(models.Movimentacao).filter(models.Movimentacao.id == movimentacao_id).first()

def get_mov_product(db: Session, product_id: int):
    return db.query(models.Movimentacao).filter(models.Movimentacao.product_id == product_id).all()

def create_movimentacao(db: Session, movimentacao: schemas.Movimentacao):
    db_mov = models.Movimentacao(amount = movimentacao.amount,
                                product_id = movimentacao.product_id)
    db.add(db_mov)
    db.commit()
    db.refresh(db_mov)
    return db_mov
