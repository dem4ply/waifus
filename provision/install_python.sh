#!/bin/bash
set -e
FILE_CHECK=~/provision_installed
touch $FILE_CHECK
if ! grep -q -m 1 'python 3.7' $FILE_CHECK;
then
	echo "================="
	echo "Instalando python"
	echo "================="

	yum update -y
	yum group install development -y
   yum install wget zlib-devel gcc openssl-devel bzip2-devel libffi-devel -y
	# yum install -y install https://centos7.iuscommunity.org/ius-release.rpm
	# yum -y install python37u python37u-pip python37u-devel git

	cd /usr/src
	wget -q https://www.python.org/ftp/python/3.7.0/Python-3.7.0.tgz
	tar xzf Python-3.7.0.tgz
	cd Python-3.7.0
	./configure --enable-optimizations
	make altinstall

	ln -s /usr/local/bin/python3.7 /usr/bin/python3
	ln -s /usr/local/bin/pip3.7 /usr/bin/pip3

	if [ ! -d ~/python_lib ]
	then
		mkdir ~/python_lib
	fi

	yum update -y

	pip3 install chibi
	pip3 install chibi-requests
	pip3 install chibi_command
	pip3 install pyyaml

	echo "python 3.7" >> $FILE_CHECK

	echo "===================================="
	echo "Terminanado la instalacion de python"
	echo "===================================="
fi
