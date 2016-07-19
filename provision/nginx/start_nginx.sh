#!/bin/bash

echo "==============="
echo "Iniciando Nginx"
echo "==============="

FOLDER_PROVISION="/home/vagrant/provision/nginx/provision"

sudo mkdir -p /var/log/gwen /var/log/nginx
sudo mkdir -p /etc/nginx/sites_available /etc/nginx/sites_enabled

sudo cp $FOLDER_PROVISION/sites_available/* /etc/nginx/sites_available/
sudo cp $FOLDER_PROVISION/conf.d/* /etc/nginx/conf.d/

sudo find /etc/nginx/sites_available/ -name "*.conf" -exec ln -s {} \
		/etc/nginx/sites_enabled/ +

sudo systemctl restart nginx

echo "==========================="
echo "Finalizado iniscio de Nginx"
echo "==========================="
