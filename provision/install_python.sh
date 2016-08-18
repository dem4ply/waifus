#!/bin/bash

FILE_CHECK="install_python"
if [ ! -f ~/$FILE_CHECK ]
then

	cowsay "Instalando python"

	FOLDER_PROVISION="/home/vagrant/provision"

	sudo yum update -y
	sudo yum install epel-release -y
	sudo yum install python34 python34-devel python-pip -y
	if [ ! -f /home/vagrant/.cache/get-pip.py ]
	then
		curl https://bootstrap.pypa.io/get-pip.py 2>/dev/null > ~/.cache/get-pip.py
	fi
	python3.4 ~/.cache/get-pip.py
	sudo yum groupinstall "Development Tools" -y
	sudo yum install python34-devel -y

	touch ~/$FILE_CHECK

	cowsay "Termianadno de instalar python"
fi

