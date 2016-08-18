#!/bin/bash
cowsay "iniciando elasticsearch for $1"
CONFIG_NAME=$1
FOLDER_PROVISION="/home/vagrant/provision/elasticsearch/provision"

sudo cp -v $FOLDER_PROVISION/$CONFIG_NAME.yml /etc/elasticsearch/elasticsearch.yml
sudo mkdir -v -p /var/data/waifus /var/log/waifus
sudo chown -v -R elasticsearch:elasticsearch /var/data/waifus
sudo chown -v -R elasticsearch:elasticsearch /var/log/waifus

if [ ! -d '/mnt/backups/waifus' ]
then
	sudo mkdir -p /mnt/backups/waifus
	sudo chown -R elasticsearch:elasticsearch /mnt/backups/
	sudo ln -s -v /mnt/backups/waifus /home/vagrant/backups/waifus
fi

sudo systemctl restart elasticsearch.service

cowsay "termino de inicar elasticsearch"
