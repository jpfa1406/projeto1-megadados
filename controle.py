from fastapi import Body, Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

#banco: List[Product] = []asyn
 
app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/products", status_code=201, tags=["Products"], summary="Creat a product")
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    """
    Create an product with all the information:

    - **id**: unique product id is auto generated
    - **name**: each item must have a name
    - **description**: optional, description of the product
    - **price**: required
    """
    return crud.create_product(db=db, product=product)

@app.get("/products", response_model=list[schemas.Product], tags=["Products"], summary="Get all products")
def get_products(db: Session = Depends(get_db), skip: int = 0, limit: int = 10):
    products = crud.get_products(db, skip=skip, limit=limit)
    return products


@app.get("/products/{product_id}", response_model=schemas.Product, tags=["Products"], summary="Get a specific product")
def get_product(product_id: int, db: Session = Depends(get_db)):
    db_product = crud.get_product(db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_product

@app.put("/products/{product_id}", response_model=schemas.ProductCreate, tags=["Products"], summary="Update a product")
def update_product(product_id: int, product: schemas.ProductCreate, db: Session = Depends(get_db)):
    """
    Update a product information:

    - **id**: unique product id is auto generated
    - **name**: each item must have a name
    - **description**: optional, description of the product
    - **price**: required

    """
    db_product = crud.get_product(db, product_id)
    if db_product:
        crud.update_product(db, product, product_id)
    else:
        raise HTTPException(status_code=404, detail="Item not found")
    return product

@app.delete("/products/{product_id}", tags=["Products"], summary="Delete a product")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    db_product = crud.get_product(db, product_id)
    if db_product:
        crud.delete_product(db, product_id)
    else:
        raise HTTPException(status_code=404, detail="Item not found")


@app.post("/movimentacoes", status_code=201, tags=["Movimentacoes"])
def create_movimentacao(movimentacao: schemas.MovimentacaoCreate, db: Session = Depends(get_db)):
    """
    Create a movimentacao with all the information:

    - **id**: unique id is auto generated
    - **amount**: quantidade movimentada
    - **product_id**: what product is related to
    """
    db_product = crud.get_product(db, movimentacao.product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Item non exintent")
    db_product.quantity += movimentacao.amount
    crud.update_product(db, db_product, movimentacao.product_id)
    return crud.create_movimentacao(db=db, movimentacao=movimentacao)

@app.get("/movimentacoes", response_model=list[schemas.Movimentacao], tags=["Movimentacoes"], summary="Get all movimentacoes")
def get_movimentacoes(db: Session = Depends(get_db), skip: int = 0, limit: int = 10):
    movimentacoes = crud.get_movimentacoes(db, skip=skip, limit=limit)
    return movimentacoes

@app.get("/movimentacoes/{movimentacao_id}", response_model=schemas.Movimentacao, tags=["Movimentacoes"], summary="Get a specific movimentacao")
def get_product(movimentacao_id: int, db: Session = Depends(get_db)):
    db_mov = crud.get_movimentacao(db, movimentacao_id=movimentacao_id)
    if db_mov is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_mov

@app.get("/products/{product_id}/movimentacoes", response_model=list[schemas.Movimentacao], tags=["Products"], summary="Get a all movimentacoes of a product")
def get_mov_product(product_id: int, db: Session = Depends(get_db)):
    db_mov_prod = crud.get_product(db, product_id=product_id)
    if db_mov_prod is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return crud.get_mov_product(db, product_id=product_id)
        



