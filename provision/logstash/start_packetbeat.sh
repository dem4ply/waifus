#!/bin/bash

config_file=$1

echo "iniciar packetbeat $config_file" | ponysay

FOLDER_PROVISION_REPO="/home/vagrant/provision/logstash/provision"
sudo cp -v $FOLDER_PROVISION_REPO/$config_file /etc/packetbeat/packetbeat.yml
sudo systemctl restart packetbeat.service

echo "terminar de iniciar packetbeat" | ponysay
