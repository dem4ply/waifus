#!/bin/bash

FILE_CHECK="install_elasticsearch"
if [ ! -f ~/$FILE_CHECK ]
then
	cowsay "instalasion elasticsearch"
	FOLDER_PROVISION_REPO="/home/vagrant/provision/repos"

	sudo rpm --import http://packages.elastic.co/GPG-KEY-elasticsearch

	sudo cp -v \
		$FOLDER_PROVISION_REPO/elasticsearch.repo /etc/yum.repos.d/elasticsearch.repo

	sudo yum -y install elasticsearch

	sudo systemctl enable elasticsearch.service
	sudo /usr/share/elasticsearch/bin/plugin install royrusso/elasticsearch-HQ

	touch ~/$FILE_CHECK

	cowsay "fin de instalasion elasticsearch"
fi
