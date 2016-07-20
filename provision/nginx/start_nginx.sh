#!/bin/bash

echo "Iniciando Nginx" | ponysay

FOLDER_PROVISION="/home/vagrant/provision/nginx/provision"

sudo mkdir -p /var/log/nginx
sudo mkdir -p /etc/nginx/sites_available /etc/nginx/sites_enabled

sudo cp -v  $FOLDER_PROVISION/sites_available/* /etc/nginx/sites_available/
sudo cp -v  $FOLDER_PROVISION/conf.d/* /etc/nginx/conf.d/
sudo cp -v  $FOLDER_PROVISION/nginx.conf /etc//nginx/nginx.conf

sudo ln -s \
	/etc/nginx/sites_available/waifus.conf \
	/etc/nginx/sites_enabled/waifus.conf

sudo ln -s \
	/etc/nginx/sites_available/waifus_elastic.conf \
	/etc/nginx/sites_enabled/waifus_elastic.conf

sudo systemctl restart nginx

echo "Finalizado iniscio de Nginx" | ponysay
