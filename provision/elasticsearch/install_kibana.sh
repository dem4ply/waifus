#!/bin/bash

FILE_CHECK=".install_kibana"
if [ ! -f ~/$FILE_CHECK ]
then
	cowsay "instalacion de kibana"

	FOLDER_PROVISION="/home/vagrant/provision"
	sudo yum update -y

	sudo yum -y install kibana

	sudo systemctl enable elasticsearch.service
	sudo systemctl start elasticsearch.service

	touch ~/$FILE_CHECK

	cowsay "fin de instalasion kibana"
fi
