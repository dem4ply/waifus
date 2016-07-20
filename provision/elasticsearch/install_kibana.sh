#!/bin/bash

FILE_CHECK="install_kibana"
if [ ! -f ~/$FILE_CHECK ]
then
	echo "instalasion de kibana" | ponysay

	FOLDER_PROVISION="/home/vagrant/provision"
	sudo yum update -y

	echo '[kibana-4.4]
name=Kibana repository for 4.4.x packages
baseurl=http://packages.elastic.co/kibana/4.4/centos
gpgcheck=1
gpgkey=http://packages.elastic.co/GPG-KEY-elasticsearch
enabled=1
' | sudo tee /etc/yum.repos.d/kibana.repo

	sudo yum -y install kibana

	sudo systemctl enable elasticsearch.service
	sudo systemctl start elasticsearch.service

	touch ~/$FILE_CHECK

	echo "fin de instalasion kibana" | ponysay
fi
