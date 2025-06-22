# my-coffee-store/backend/Dockerfile

# 使用 Python 3.9 的官方 Alpine 基礎映像，它體積較小
FROM python:3.9-alpine

# 設定工作目錄
WORKDIR /app

# 安裝 PostgreSQL 客戶端開發庫
# 這是 psycopg2-binary 正常工作所必需的
RUN apk add --no-cache postgresql-dev gcc python3-dev musl-dev

# 複製依賴文件並安裝
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 複製應用程式程式碼
COPY app/ app/

# 暴露應用程式運行的端口
EXPOSE 8000

# 定義應用程式啟動命令
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
# 這裡不使用 CMD，因為 docker-compose.yaml 中會覆蓋它來運行 migration 和 app