FROM python:2.7

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client libssl-dev ca-certificates \
        python-setuptools \
    && rm -rf /var/lib/apt/lists/*

# nginx sources
RUN curl --location http://nginx.org/keys/nginx_signing.key > nginx_signing.key
RUN apt-key add nginx_signing.key
RUN echo "deb http://nginx.org/packages/ubuntu/ trusty nginx" >> /etc/apt/sources.list
RUN echo "deb-src http://nginx.org/packages/ubuntu/ trusty nginx" >> /etc/apt/sources.list

RUN apt-get update

# Forward nginx logs to docker log collector
RUN mkdir -p /var/log/nginx
RUN touch /var/log/nginx/access.log
RUN touch /var/log/nginx/error.log
RUN ln -sf /dev/stdout /var/log/nginx/access.log
RUN ln -sf /dev/stderr /var/log/nginx/error.log
RUN mkdir -p /var/log/gunicorn
RUN touch /var/log/gunicorn/access.log
RUN ln -sf /dev/stdout /var/log/gunicorn/access.log

# Install nginx
RUN apt-get update && \
 apt-get install -y nginx

# Install dependencies
RUN mkdir -p /var/apps/apple-devices-locator
WORKDIR /var/apps/apple-devices-locator/
COPY requirements.txt ./
RUN pip install -r requirements.txt

# Install OAuth2 Proxy
ENV OAUTH2_PROXY_URL "https://github.com/bitly/oauth2_proxy/releases/download/v2.0.1/oauth2_proxy-2.0.1.linux-amd64.go1.4.2.tar.gz"
WORKDIR /tmp
RUN curl -L $OAUTH2_PROXY_URL > oauth2_proxy.tar.gz
RUN tar xzvf oauth2_proxy.tar.gz
RUN mv /tmp/oauth2_proxy-2.0.1.linux-amd64.go1.4.2/oauth2_proxy /usr/bin/oauth2_proxy
RUN chmod +x /usr/bin/oauth2_proxy

# Install Configure supervisord
RUN /usr/bin/easy_install supervisor
RUN /usr/bin/easy_install supervisor-stdout

ADD ./docker/supervisord-web.conf /etc/supervisord-web.conf

# Copy and setup project
COPY . /var/apps/apple-devices-locator
RUN chmod +x /var/apps/apple-devices-locator/docker/start_web.sh

ENV PYTHONUNBUFFERED 1
WORKDIR /var/apps/apple-devices-locator

EXPOSE 80
ENV PORT 80

# Start gunicorn
CMD ./docker/start_web.sh
