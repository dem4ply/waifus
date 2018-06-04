#!/bin/bash

FILE_CHECK=~/provision_installed
touch $FILE_CHECK
if ! grep -q -m 1 'python 3.6' $FILE_CHECK;
then
	echo "================="
	echo "Instalando python"
	echo "================="

	yum update -y
	yum groupinstall development -y
	yum groupinstall "Development Tools" -y
	yum install zlib-devel -y
	yum install -y install https://centos7.iuscommunity.org/ius-release.rpm
	yum -y install python36u python36u-pip python36u-devel git

	ln -s /usr/bin/python3.6 /usr/bin/python3

	if [ ! -d ~/python_lib ]
	then
		mkdir ~/python_lib
	fi
	cd ~/python_lib
	git clone https://github.com/dem4ply/chibi.git
	pip3.6 install ./chibi
	pip3.6 install pyyaml

	echo "python 3.6" >> $FILE_CHECK

	echo "===================================="
	echo "Terminanado la instalacion de python"
	echo "===================================="
fi
