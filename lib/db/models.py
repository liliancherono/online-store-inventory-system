from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from ..database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True)
    price = Column(Float, nullable=False)
    stock_quantity = Column(Integer, nullable=False, default=0)

    # Relationship with Order
    orders = relationship("Order", back_populates="product", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Product(name={self.name}, price={self.price}, stock={self.stock_quantity})>"


class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone = Column(String, unique=True, nullable=False)

    # Relationship with Order
    orders = relationship("Order", back_populates="customer", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Customer(name={self.name}, email={self.email})>"


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("customers.id", ondelete="CASCADE"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id", ondelete="CASCADE"), nullable=False)
    quantity = Column(Integer, nullable=False, default=1)

    # Relationships
    customer = relationship("Customer", back_populates="orders")
    product = relationship("Product", back_populates="orders")

    def __repr__(self):
        return f"<Order(customer={self.customer_id}, product={self.product_id}, quantity={self.quantity})>"
