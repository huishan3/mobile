# my-coffee-store/backend/app/main.py

from fastapi import FastAPI, Depends, HTTPException, status, Form
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session, joinedload # 導入 joinedload
from typing import List, Optional
from datetime import timedelta
import os

from . import models, schemas, auth
from .database import engine, get_db
from fastapi.middleware.cors import CORSMiddleware

# 創建所有在 models.py 中定義的資料庫表格
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Melody Beans Coffee Shop API",
    description="Backend API for the Melody Beans coffee shop, handling users, products, orders, and reviews.",
    version="0.1.0",
)

# 設置 CORS (跨來源資源共享) 中間件
origins = [
    "http://localhost",
    "http://localhost:80",
    "http://localhost:3000", # 通常 React/Vue 開發服務器使用的端口
    "http://frontend", # Docker 內部的前端服務名稱
    "http://backend", # Docker 內部的後端服務名稱 (作為 fallback，雖然通常不需要)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ==================== 用戶認證相關 API ====================

@app.post("/api/auth/register", response_model=schemas.UserResponse, status_code=status.HTTP_201_CREATED)
async def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user_username = db.query(models.User).filter(models.User.username == user.username).first()
    if db_user_username:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="用戶名已被註冊")
    db_user_email = db.query(models.User).filter(models.User.email == user.email).first()
    if db_user_email:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="電子郵件已被註冊")
    hashed_password = auth.get_password_hash(user.password)
    db_user = models.User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password,
        full_name=user.full_name,
        is_admin=user.is_admin # 允許在註冊時設置管理員權限，但通常會通過其他方式管理
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.post("/api/auth/login", response_model=schemas.Token)
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    user = auth.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="不正確的用戶名或密碼",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=auth.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = auth.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/api/auth/me", response_model=schemas.UserResponse)
async def read_users_me(current_user: models.User = Depends(auth.get_current_user)):
    return current_user

# ==================== 商品相關 API ====================

@app.post("/api/products/", response_model=schemas.ProductResponse, status_code=status.HTTP_201_CREATED)
async def create_product(
    product: schemas.ProductCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_admin_user) # 只有管理員可以創建商品
):
    db_product = models.Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

@app.get("/api/products/", response_model=List[schemas.ProductResponse])
async def read_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    products = db.query(models.Product).offset(skip).limit(limit).all()
    return products

@app.get("/api/products/{product_id}", response_model=schemas.ProductResponse)
async def read_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if product is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="商品未找到")
    return product

@app.put("/api/products/{product_id}", response_model=schemas.ProductResponse)
async def update_product(
    product_id: int,
    product: schemas.ProductCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_admin_user) # 只有管理員可以更新商品
):
    db_product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if db_product is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="商品未找到")
    for key, value in product.dict(exclude_unset=True).items():
        setattr(db_product, key, value)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

@app.delete("/api/products/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(
    product_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_admin_user) # 只有管理員可以刪除商品
):
    db_product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if db_product is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="商品未找到")
    db.delete(db_product)
    db.commit()
    return {"message": "商品已刪除"}

# ==================== 評論相關 API ====================

@app.post("/api/reviews/", response_model=schemas.ReviewResponse, status_code=status.HTTP_201_CREATED)
async def create_review(
    review: schemas.ReviewCreate,
    db: Session = Depends(get_db)
    # current_user: models.User = Depends(auth.get_current_user) # 實際應用中，會從這裡獲取 user_id
):
    """
    創建新評論。
    注意：目前 user_id 從請求體中獲取，在有完整用戶認證系統後應從 token 中獲取。
    """
    user = db.query(models.User).filter(models.User.id == review.user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"用戶ID {review.user_id} 未找到。請確保該用戶已註冊。")

    if review.product_id:
        product = db.query(models.Product).filter(models.Product.id == review.product_id).first()
        if not product:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="評論商品未找到")

    db_review = models.Review(
        user_id=review.user_id,
        product_id=review.product_id,
        rating=review.rating,
        comment=review.comment
    )
    db.add(db_review)
    db.commit()
    db.refresh(db_review)

    # 確保返回時加載了 user 和 product 關係
    db_review.user = user
    if review.product_id:
        db_review.product = product

    return db_review


@app.get("/api/reviews/", response_model=List[schemas.ReviewResponse])
async def read_reviews(
    product_id: Optional[int] = None,
    user_id: Optional[int] = None,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """
    獲取所有評論列表，可按商品 ID 或用戶 ID 過濾。
    同時加載關聯的用戶和產品信息。
    """
    query = db.query(models.Review)
    if product_id:
        query = query.filter(models.Review.product_id == product_id)
    if user_id:
        query = query.filter(models.Review.user_id == user_id)
    
    # 使用 joinedload 來一次性加載關聯數據，減少 N+1 查詢問題
    reviews = query.options(
        joinedload(models.Review.user),
        joinedload(models.Review.product)
    ).offset(skip).limit(limit).all()

    return reviews

@app.get("/api/reviews/{review_id}", response_model=schemas.ReviewResponse)
async def read_review(review_id: int, db: Session = Depends(get_db)):
    """
    根據 ID 獲取單個評論詳細資訊，並加載關聯的用戶和產品信息。
    """
    review = db.query(models.Review).options(
        joinedload(models.Review.user),
        joinedload(models.Review.product)
    ).filter(models.Review.id == review_id).first()

    if review is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="評論未找到")
    return review

@app.delete("/api/reviews/{review_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_review(
    review_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_admin_user) # 只有管理員可以刪除評論
):
    db_review = db.query(models.Review).filter(models.Review.id == review_id).first()
    if db_review is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="評論未找到")
    db.delete(db_review)
    db.commit()
    return {"message": "評論已刪除"}


# ==================== 訂單相關 API ====================

@app.post("/api/orders/", response_model=schemas.OrderResponse, status_code=status.HTTP_201_CREATED)
async def create_order(
    order_data: schemas.OrderCreate,
    db: Session = Depends(get_db)
    # current_user: models.User = Depends(auth.get_current_user) # 實際應用中，會從這裡獲取 user_id
):
    """
    創建新訂單。
    注意：目前 user_id 暫時硬編碼為 1，在有完整用戶認證系統後應從 token 中獲取。
    """
    # 假設用戶 ID 為 1。在真實應用中，這應該是 current_user.id
    user_id = 1
    existing_user = db.query(models.User).filter(models.User.id == user_id).first()
    if not existing_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"用戶ID {user_id} 未找到。請確保該用戶已註冊。")

    products_in_order = {}
    for item in order_data.items:
        product = db.query(models.Product).filter(models.Product.id == item.product_id).first()
        if not product:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"商品ID {item.product_id} 未找到")
        if item.quantity <= 0:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"商品ID {item.product_id} 的數量必須大於0")
        products_in_order[item.product_id] = product

    db_order = models.Order(
        user_id=user_id,
        total_amount=order_data.total_amount,
        shipping_address=order_data.shipping_address,
        payment_method=order_data.payment_method,
        recipient_name=order_data.recipient_name,
        recipient_phone=order_data.recipient_phone
    )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)

    for item in order_data.items:
        product = products_in_order[item.product_id]
        db_order_item = models.OrderItem(
            order_id=db_order.id,
            product_id=item.product_id,
            quantity=item.quantity,
            price_at_order=product.price
        )
        db.add(db_order_item)
    db.commit()
    db.refresh(db_order)

    # 確保返回時加載了 user 和 items 以及 item 中的 product 關係
    order_with_relations = db.query(models.Order).options(
        joinedload(models.Order.user),
        joinedload(models.Order.items).joinedload(models.OrderItem.product)
    ).filter(models.Order.id == db_order.id).first()

    return order_with_relations


@app.get("/api/orders/", response_model=List[schemas.OrderResponse])
async def read_orders(
    user_id: Optional[int] = None,
    status: Optional[str] = None,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
    # current_user: models.User = Depends(auth.get_current_user) # 在真實應用中，用戶只能查看自己的訂單
):
    """
    獲取所有訂單列表，可按用戶 ID 或狀態過濾。
    加載關聯的用戶和訂單商品信息。
    """
    query = db.query(models.Order)
    if user_id:
        query = query.filter(models.Order.user_id == user_id)
    if status:
        query = query.filter(models.Order.status == status)

    orders = query.options(
        joinedload(models.Order.user),
        joinedload(models.Order.items).joinedload(models.OrderItem.product)
    ).offset(skip).limit(limit).all()

    return orders

@app.get("/api/orders/{order_id}", response_model=schemas.OrderResponse)
async def read_order(
    order_id: int,
    db: Session = Depends(get_db)
    # current_user: models.User = Depends(auth.get_current_user) # 在真實應用中，用戶只能查看自己的訂單
):
    """
    根據 ID 獲取單個訂單詳細資訊，並加載關聯的用戶和訂單商品信息。
    """
    order = db.query(models.Order).options(
        joinedload(models.Order.user),
        joinedload(models.Order.items).joinedload(models.OrderItem.product)
    ).filter(models.Order.id == order_id).first()

    if order is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="訂單未找到")
    return order

@app.put("/api/orders/{order_id}/status", response_model=schemas.OrderResponse)
async def update_order_status(
    order_id: int,
    status: str = Form(...),
    db: Session = Depends(get_db),
    current_admin_user: models.User = Depends(auth.get_current_admin_user) # 只有管理員可以更新訂單狀態
):
    db_order = db.query(models.Order).filter(models.Order.id == order_id).first()
    if db_order is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="訂單未找到")

    valid_statuses = ["pending", "processing", "completed", "cancelled"]
    if status not in valid_statuses:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"無效的訂單狀態。有效狀態為: {', '.join(valid_statuses)}")

    db_order.status = status
    db.add(db_order)
    db.commit()
    db.refresh(db_order)

    # 加載關聯數據以便響應
    # 這裡重新查詢一次，確保所有關係都已加載，或者可以直接使用 joinedload
    order_with_relations = db.query(models.Order).options(
        joinedload(models.Order.user),
        joinedload(models.Order.items).joinedload(models.OrderItem.product)
    ).filter(models.Order.id == db_order.id).first()
    
    return order_with_relations

@app.delete("/api/orders/{order_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_order(
    order_id: int,
    db: Session = Depends(get_db),
    current_admin_user: models.User = Depends(auth.get_current_admin_user) # 只有管理員可以刪除訂單
):
    db_order = db.query(models.Order).filter(models.Order.id == order_id).first()
    if db_order is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="訂單未找到")
    db.delete(db_order)
    db.commit()
    return {"message": "訂單已刪除"}
# 在 main.py 中添加此段代碼
@app.get("/api/reviews/", response_model=List[schemas.ReviewResponse])
async def read_all_reviews(
    db: Session = Depends(get_db),
    current_admin_user: models.User = Depends(auth.get_current_admin_user) # 僅限管理員
):
    """
    獲取所有評論 (僅限管理員)
    """
    reviews = db.query(models.Review).options(
        joinedload(models.Review.user),
        joinedload(models.Review.product)
    ).all()
    return reviews