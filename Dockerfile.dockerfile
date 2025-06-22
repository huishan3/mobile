# my-coffee-store/frontend/Dockerfile
FROM nginx:alpine

# 將你的自定義 nginx.conf 複製到 Nginx 配置目錄
# 這會替換掉 conf.d 中的 default.conf
COPY ./nginx.conf /etc/nginx/conf.d/default.conf

# 將你的靜態網站文件複製到 Nginx 的網站根目錄
COPY ./html /usr/share/nginx/html