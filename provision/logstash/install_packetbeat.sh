#!/bin/bash

FILE_CHECK="install_packetbeat"
if [ ! -f ~/$FILE_CHECK ]
then
	echo "instalasion packetbeat" | ponysay
	FOLDER_PROVISION_REPO="/home/vagrant/provision/repos"

	sudo rpm --import http://packages.elastic.co/GPG-KEY-elasticsearch
	sudo cp -v $FOLDER_PROVISION_REPO/beats.repo /etc/yum.repos.d/beats.repo

	sudo yum -y install packetbeat
	sudo systemctl enable packetbeat.service

	touch ~/$FILE_CHECK
	topecho "fin de instalasion de packetbeat" | ponysay
fi
