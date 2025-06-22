# my-coffee-store/backend/app/models.py

from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .database import Base

# 用戶模型
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    full_name = Column(String, nullable=True)
    is_admin = Column(Boolean, default=False)

    reviews = relationship("Review", back_populates="user")
    orders = relationship("Order", back_populates="user")

# 商品模型
class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    description = Column(String, nullable=True)
    price = Column(Float, nullable=False)
    image_url = Column(String, nullable=True) # 商品圖片 URL
    is_available = Column(Boolean, default=True) # 是否上架

    reviews = relationship("Review", back_populates="product")
    order_items = relationship("OrderItem", back_populates="product")

# 評論模型
class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=True) # 評論可以針對商品，也可以是整體服務
    rating = Column(Integer, nullable=False) # 評分 (1-5星)
    comment = Column(Text, nullable=True) # 評論內容
    created_at = Column(DateTime, server_default=func.now())

    user = relationship("User", back_populates="reviews")
    product = relationship("Product", back_populates="reviews")

# 訂單模型
class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    total_amount = Column(Float, nullable=False)
    status = Column(String, default="pending")
    shipping_address = Column(Text, nullable=False)
    payment_method = Column(String, nullable=False)
    recipient_name = Column(String, nullable=False)
    recipient_phone = Column(String, nullable=False)

    created_at = Column(DateTime, server_default=func.now())

    user = relationship("User", back_populates="orders")
    items = relationship("OrderItem", back_populates="order", cascade="all, delete-orphan")

# 訂單項目模型
class OrderItem(Base):
    __tablename__ = "order_items"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    quantity = Column(Integer, nullable=False)
    price_at_order = Column(Float, nullable=False) # 記錄下單時的商品價格

    order = relationship("Order", back_populates="items")
    product = relationship("Product", back_populates="order_items")