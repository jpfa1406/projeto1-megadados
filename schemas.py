from typing import Union
from pydantic import BaseModel

class ProductBase(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "name": "nova_string",
                "description": "nova_string",
                "price": 6.29
            }
        }