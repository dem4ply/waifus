#!/bin/bash

FILE_CHECK=".install_kibana_dashboards"
if [ ! -f ~/$FILE_CHECK ]
then
	cowsay "instalasion daskboards de kibana"
	FOLDER_PROVISION_REPO="/home/vagrant/provision/repo"

	sudo apt-get -y install unzip

	cd /tmp/

	curl -L -O https://download.elastic.co/beats/dashboards/beats-dashboards-1.1.0.zip

	unzip beats-dashboards-*.zip
	cd beats-dashboards-*
	./load.sh -l spider-verse:80
	cd ~

	touch ~/$FILE_CHECK

	cowsay "fin de instalasion de los dashboards de kibana"
fi
