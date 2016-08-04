#!/bin/bash

FILE_CHECK="install_topbeat"
if [ ! -f ~/$FILE_CHECK ]
then
	echo "instalasion topbeat" | ponysay
	FOLDER_PROVISION_REPO="/home/vagrant/provision/repos"

	sudo rpm --import http://packages.elastic.co/GPG-KEY-elasticsearch
	sudo cp -v $FOLDER_PROVISION_REPO/beats.repo /etc/yum.repos.d/beats.repo

	sudo yum -y install topbeat
	sudo systemctl enable topbeat.service

	touch ~/$FILE_CHECK
	echo "fin de instalasion de topbeat" | ponysay
fi
