FROM ubuntu:14.04
RUN apt-get update && apt-get install -y nginx
RUN echo 'Hi, I am in your container' \ 
>/usr/share/nginx/html/index.html
EXPOSE 80
