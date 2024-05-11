FROM nginx:alpine

# HTML、CSS、JSファイルをコピー
COPY ./command.html /usr/share/nginx/html/command.html
COPY ./style.css /usr/share/nginx/html/style.css
COPY ./script.js /usr/share/nginx/html/script.js

# Nginxの設定ファイルをコピー
COPY ./default.conf /etc/nginx/conf.d/default.conf

EXPOSE 80