#!/bin/bash
FILE_CHECK="install_nginx"
if [ ! -f ~/$FILE_CHECK ]
then

	echo "================"
	echo "Instalando Nginx"
	echo "================"
	FOLDER_PROVISION="/home/vagrant/provision"
	sudo yum update -y
	sudo yum install -y epel-release

	sudo yum -y install nginx
	sudo systemctl enable nginx
	sudo systemctl start nginx

	touch ~/$FILE_CHECK
	echo "============================"
	echo "Finalizado instalasion Nginx"
	echo "============================"
fi
