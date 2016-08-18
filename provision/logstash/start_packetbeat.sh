#!/bin/bash

config_file=$1

cowsay "iniciar packetbeat $config_file"

FOLDER_PROVISION_REPO="/home/vagrant/provision/logstash/provision"
sudo cp -v $FOLDER_PROVISION_REPO/$config_file /etc/packetbeat/packetbeat.yml
sudo systemctl restart packetbeat.service

cowsay "terminar de iniciar packetbeat"
