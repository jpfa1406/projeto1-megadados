from typing import Union
from pydantic import BaseModel

class Product(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float

    class Config:
        schema_extra = {
            "example": {
                "name": "Bis",
                "description": "Chocolate nestle bis branco laka 2kg",
                "price": 6.29
            }
        }