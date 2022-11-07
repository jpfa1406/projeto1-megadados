from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from .database import Base


#class User(Base):
#    __tablename__ = "products"
#
#    id = Column(Integer, primary_key=True, index=True)
#    email = Column(String, unique=True, index=True)
#    hashed_password = Column(String)
#    is_active = Column(Boolean, default=True)
#
#    items = relationship("Item", back_populates="owner")


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(80))
    description = Column(String(300))
    price = Column(Float)
    quantity = Column(Integer)

class Movimentacao(Base):
    __tablename__ = "movimentacoes"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Integer)
    product_id = Column(Integer, ForeignKey("products.id"))
