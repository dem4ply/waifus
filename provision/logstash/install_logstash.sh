#!/bin/bash

FILE_CHECK="install_logstash"
if [ ! -f ~/$FILE_CHECK ]
then
	echo "instalasion logstash" | ponysay
	FOLDER_PROVISION_REPO="/home/vagrant/provision/repos"

	sudo rpm --import http://packages.elastic.co/GPG-KEY-elasticsearch
	sudo cp -v \
		$FOLDER_PROVISION_REPO/logstash.repo /etc/yum.repos.d/logstash.repo

	sudo yum -y install logstash
	sudo systemctl enable logstash.service

	touch ~/$FILE_CHECK
	echo "fin de instalasion de logstash" | ponysay
fi
