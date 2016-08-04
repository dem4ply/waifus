#!/bin/bash

config_file=$1

echo "iniciar topbeat $config_file" | ponysay

FOLDER_PROVISION_REPO="/home/vagrant/provision/logstash/provision"
sudo cp -v $FOLDER_PROVISION_REPO/$config_file /etc/topbeat/topbeat.yml
sudo systemctl restart topbeat.service

echo "terminar de iniciar topbeat" | ponysay
