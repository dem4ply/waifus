#!/bin/bash
echo "iniciando elasticsearch for $1" | ponysay
CONFIG_NAME=$1
FOLDER_PROVISION="/home/vagrant/provision/elasticsearch/provision"

sudo cp $FOLDER_PROVISION/$CONFIG_NAME.yml /etc/elasticsearch/elasticsearch.yml
sudo mkdir -p /var/data/waifus /var/log/waifus
sudo chown -R elasticsearch:elasticsearch /var/data/waifus
sudo chown -R elasticsearch:elasticsearch /var/log/waifus

sudo systemctl restart elasticsearch.service

echo "termino de inicar elasticsearch" | ponysay
