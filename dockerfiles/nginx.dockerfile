FROM nginx:latest

WORKDIR /app

COPY ./services/nginx.config /etc/nginx/conf.d/default.conf

EXPOSE 8080