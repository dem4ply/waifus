#!/bin/bash

FILE_CHECK="install_elasticsearch"
if [ ! -f ~/$FILE_CHECK ]
then
	echo "instalasion elasticsearch" | ponysay

	FOLDER_PROVISION="/home/vagrant/provision"
	sudo yum update -y
	sudo rpm -iUvh http://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-release-7-5.noarch.rpm

	sudo yum groupinstall "Development Tools" -y

	# download java
	wget --no-cookies --no-check-certificate \
		-O /tmp/java.rpm \
		--header "Cookie: gpw_e24=http%3A%2F%2Fwww.oracle.com%2F; oraclelicense=accept-securebackup-cookie"\
		"http://download.oracle.com/otn-pub/java/jdk/8u73-b02/jdk-8u73-linux-x64.rpm"

	sudo yum -y localinstall /tmp/java.rpm

	sudo rpm --import http://packages.elastic.co/GPG-KEY-elasticsearch

	echo '[elasticsearch-2.x]
name=Elasticsearch repository for 2.x packages
baseurl=http://packages.elastic.co/elasticsearch/2.x/centos
gpgcheck=1
gpgkey=http://packages.elastic.co/GPG-KEY-elasticsearch
enabled=1
' | sudo tee /etc/yum.repos.d/elasticsearch.repo

	sudo yum -y install elasticsearch

	sudo systemctl enable elasticsearch.service
	sudo /usr/share/elasticsearch/bin/plugin install royrusso/elasticsearch-HQ

	touch ~/$FILE_CHECK

	echo "fin de instalasion elasticsearch" | ponysay
fi
