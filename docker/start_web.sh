#!/bin/bash
echo configuring nginx
cat ./docker/nginx.conf > /etc/nginx/nginx.conf
cat ./docker/nginx.apple-devices-locator.conf > /etc/nginx/conf.d/default.conf

echo configuring oauth2_proxy
cat ./docker/oauth2_proxy.config > /etc/oauth2_proxy.config
sed -i -e "s/{{OAUTH2_PROXY_CLIENT_ID}}/$OAUTH2_PROXY_CLIENT_ID/g" /etc/oauth2_proxy.config
sed -i -e "s/{{OAUTH2_PROXY_CLIENT_SECRET}}/$OAUTH2_PROXY_CLIENT_SECRET/g" /etc/oauth2_proxy.config
sed -i -e "s/{{OAUTH2_PROXY_COOKIE_SECRET}}/$OAUTH2_PROXY_COOKIE_SECRET/g" /etc/oauth2_proxy.config
sed -i -e "s/{{OAUTH2_PROXY_COOKIE_DOMAIN}}/$OAUTH2_PROXY_COOKIE_DOMAIN/g" /etc/oauth2_proxy.config
sed -i -e "s|{{OAUTH2_PROXY_REDIRECT_URL}}|$OAUTH2_PROXY_REDIRECT_URL|g" /etc/oauth2_proxy.config

echo starting apple-devices-locator web ui
/usr/local/bin/supervisord -c /etc/supervisord-web.conf
