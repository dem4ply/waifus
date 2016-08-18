#!/bin/bash

config_file=$1

cowsay "iniciar topbeat $config_file"

FOLDER_PROVISION_REPO="/home/vagrant/provision/logstash/provision"
sudo cp -v $FOLDER_PROVISION_REPO/$config_file /etc/topbeat/topbeat.yml
sudo systemctl restart topbeat.service

cowsay "terminar de iniciar topbeat"
