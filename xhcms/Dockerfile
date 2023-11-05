FROM php:5.6.9-apache
RUN docker-php-ext-install mysql mysqli pdo pdo_mysql fileinfo mbstring
RUN echo 'deb http://mirrors.tencent.com/debian-archive/debian stretch main' > /etc/apt/sources.list
RUN echo 'deb http://mirrors.tencent.com/debian-archive/debian-security stretch/updates main' >> /etc/apt/sources.list
ADD entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/bin/bash", "/entrypoint.sh"]
