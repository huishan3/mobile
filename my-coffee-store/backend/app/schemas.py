# my-coffee-store/backend/app/schemas.py

from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional
from datetime import datetime

# 用戶相關 Schemas

class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    password: str = Field(..., min_length=6, max_length=100)
    full_name: Optional[str] = Field(None, max_length=100)
    is_admin: bool = False # 允許在創建時指定是否為管理員，但通常只由後端管理員設置

class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    full_name: Optional[str] = None
    is_admin: bool

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

# 商品相關 Schemas

class ProductCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    price: float = Field(..., gt=0)
    image_url: Optional[str] = None
    is_available: bool = True

class ProductResponse(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float
    image_url: Optional[str] = None
    is_available: bool

    class Config:
        from_attributes = True

# 評論相關 Schemas

class ReviewCreate(BaseModel):
    user_id: int # 在沒有認證系統的情況下，前端需要提供用戶ID
    product_id: Optional[int] = None
    rating: int = Field(..., ge=1, le=5) # 評分必須在 1 到 5 之間
    comment: str = Field(..., min_length=1, max_length=500) # 評論內容

class ReviewResponse(BaseModel):
    id: int
    user_id: int
    product_id: Optional[int] = None
    rating: int
    comment: str
    created_at: datetime
    user: Optional[UserResponse] = None # 嵌套 UserResponse
    product: Optional[ProductResponse] = None # 嵌套 ProductResponse

    class Config:
        from_attributes = True
        json_encoders = {datetime: lambda v: v.isoformat()}

# 訂單相關 Schemas

class OrderItemBase(BaseModel):
    product_id: int
    quantity: int = Field(..., gt=0)

class OrderCreate(BaseModel):
    items: List[OrderItemBase] = Field(..., min_length=1)
    total_amount: float = Field(..., gt=0)
    shipping_address: str = Field(..., min_length=1)
    payment_method: str = Field(..., min_length=1)
    recipient_name: str = Field(..., min_length=1)
    recipient_phone: str = Field(..., min_length=1)

class OrderItemResponse(OrderItemBase):
    id: int
    order_id: int
    price_at_order: float
    product: Optional[ProductResponse] = None

    class Config:
        from_attributes = True

class OrderResponse(BaseModel):
    id: int
    user_id: int
    total_amount: float
    status: str
    shipping_address: str
    payment_method: str
    recipient_name: str
    recipient_phone: str
    created_at: datetime
    user: Optional[UserResponse] = None
    items: List[OrderItemResponse] = []

    class Config:
        from_attributes = True
        json_encoders = {datetime: lambda v: v.isoformat()}