#!/bin/bash

FILE_CHECK="install_python"
if [ ! -f ~/$FILE_CHECK ]
then

	echo "================="
	echo "Instalando python"
	echo "================="

	FOLDER_PROVISION="/home/vagrant/provision"

	sudo yum update -y
	sudo yum install epel-release -y
	sudo yum install python34 python34-devel python-pip -y
	curl https://bootstrap.pypa.io/get-pip.py | python3.4
	sudo yum groupinstall "Development Tools" -y
	sudo yum install python34-devel -y

	touch ~/$FILE_CHECK

	echo "=============================="
	echo "Termianadno de instalar python"
	echo "=============================="
fi

