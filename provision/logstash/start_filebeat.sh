#!/bin/bash

config_file=$1

cowsay "iniciar filebeat $config_file"

FOLDER_PROVISION_REPO="/home/vagrant/provision/logstash/provision"
sudo cp -v $FOLDER_PROVISION_REPO/$config_file /etc/filebeat/filebeat.yml
sudo systemctl restart filebeat.service

cowsay "terminar de iniciar filebeat"
