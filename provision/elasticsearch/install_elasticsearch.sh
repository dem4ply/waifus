#!/bin/bash

FILE_CHECK="install_elasticsearch"
if [ ! -f ~/$FILE_CHECK ]
then
	echo "instalasion elasticsearch" | ponysay
	FOLDER_PROVISION_REPO="/home/vagrant/provision/repo"

	sudo rpm --import http://packages.elastic.co/GPG-KEY-elasticsearch

	sudo cp -v \
		$FOLDER_PROVISION_REPO/elasticsearch.repo /etc/yum.repos.d/elasticsearch.repo

	sudo yum -y install elasticsearch

	sudo systemctl enable elasticsearch.service
	sudo /usr/share/elasticsearch/bin/plugin install royrusso/elasticsearch-HQ

	touch ~/$FILE_CHECK

	echo "fin de instalasion elasticsearch" | ponysay
fi
