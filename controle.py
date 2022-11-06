from fastapi import Body, FastAPI, HTTPException
from models import Product
from typing import List

banco: List[Product] = []
 
app = FastAPI()

@app.post("/products", status_code=201, tags=["Products"], summary="Creat a product")
async def create_product(product: Product):
    """
    Create an product with all the information:

    - **id**: unique product id is auto generated
    - **name**: each item must have a name
    - **description**: optional, description of the product
    - **price**: required
    """
    banco.append(product)
    return product

@app.get("/products", tags=["Products"], summary="Get all products")
async def get_products():
    return banco


@app.get("/products/{product_id}", tags=["Products"], summary="Get a specific product")
async def get_product(product_id: int):
    if product_id > len(banco):
        raise HTTPException(status_code=404, detail="Item not found")
    return banco[product_id]

@app.put("/products/{product_id}", tags=["Products"], summary="Update a product")
async def update_product(
    product_id: int,
    product: Product = Body(
        example={
            "name": "Bis",
            "description": "Chocolate bis branco laka 126g",
            "price": 6.50
        },
    ),
):
    """
    Update a product information:

    - **id**: unique product id is auto generated
    - **name**: each item must have a name
    - **description**: optional, description of the product
    - **price**: required
    """

    if product_id > len(banco):
        raise HTTPException(status_code=404, detail="Product id not found")

    old_prod = banco[product_id]

    old_prod.name = product.name
    old_prod.description = product.description
    old_prod.price = product.price

    return old_prod
