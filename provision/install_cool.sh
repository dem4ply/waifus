#!/bin/bash

FILE_CHECK="install_cool"

if [ ! -f ~/$FILE_CHECK ]
then
	echo "======================"
	echo "Instalando cool things"
	echo "======================"

	sudo yum install epel-release -y
	sudo yum install fortune-mod git vim ruby -y
	sudo yum install texinfo -y

	cd /home/vagrant/.cache

	if [ ! -d ponysay ]
	then
		git clone https://github.com/erkin/ponysay.git
	fi
	cd ponysay
	sudo ./setup.py  install --freedom=partial

	cd ~
	touch ~/$FILE_CHECK
	echo "fin de Instalando cool things" | ponysay
fi
