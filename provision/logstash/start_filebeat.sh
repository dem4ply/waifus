#!/bin/bash

config_file=$1

echo "iniciar filebeat $config_file" | ponysay

FOLDER_PROVISION_REPO="/home/vagrant/provision/logstash/provision"
sudo cp -v $FOLDER_PROVISION_REPO/$config_file /etc/filebeat/filebeat.yml
sudo systemctl restart filebeat.service

echo "terminar de iniciar filebeat" | ponysay
