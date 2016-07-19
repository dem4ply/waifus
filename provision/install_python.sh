#!/bin/bash
FILE_CHECK="install_python"
if [ ! -f ~/$FILE_CHECK ]
then

	FOLDER_PROVISION="/home/vagrant/provision"
	sudo yum update -y
	sudo yum groupinstall "Development Tools" -y
	wget --directory-prefix=/tmp/ https://www.python.org/ftp/python/3.5.1/Python-3.5.1.tgz

	cd /tmp/
	tar xzf Python-3.5.1.tgz
	cd Python-3.5.1

	./configure --prefix=/usr/local

	make altinstall

	touch ~/$FILE_CHECK
fi
