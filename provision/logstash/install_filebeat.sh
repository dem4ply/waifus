#!/bin/bash

FILE_CHECK="install_filebeat"
if [ ! -f ~/$FILE_CHECK ]
then
	echo "instalasion filebeat" | ponysay
	FOLDER_PROVISION_REPO="/home/vagrant/provision/repos"

	sudo rpm --import http://packages.elastic.co/GPG-KEY-elasticsearch
	sudo cp -v $FOLDER_PROVISION_REPO/beats.repo /etc/yum.repos.d/beats.repo

	sudo yum -y install filebeat
	sudo systemctl enable filebeat.service

	touch ~/$FILE_CHECK
	echo "fin de instalasion de filebeat" | ponysay
fi
