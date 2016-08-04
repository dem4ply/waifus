#!/bin/bash
echo "iniciando elasticsearch for $1" | ponysay
CONFIG_NAME=$1
FOLDER_PROVISION="/home/vagrant/provision/elasticsearch/provision"

sudo cp $FOLDER_PROVISION/$CONFIG_NAME.yml /etc/elasticsearch/elasticsearch.yml
sudo mkdir -p /var/data/spider_verse /var/log/spider_verse
sudo chown -R elasticsearch:elasticsearch /var/data/spider_verse
sudo chown -R elasticsearch:elasticsearch /var/log/spider_verse

if [ ! -d '/mnt/backups/spider_verse' ]
then
	sudo mkdir -p /mnt/backups/spider_verse
	sudo chown -R elasticsearch:elasticsearch /mnt/backups/
	sudo ln -s -v /mnt/backups/spider_verse /home/vagrant/backups/spider_verse
fi

sudo systemctl restart elasticsearch.service


echo "termino de inicar elasticsearch" | ponysay
