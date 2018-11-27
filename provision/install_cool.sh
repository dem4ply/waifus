#!/bin/bash
FILE_CHECK=".install_cool"

if [ ! -f ~/$FILE_CHECK ]
then
	cowsay "Instalando cool things"

	sudo yum install epel-release -y
	sudo yum install fortune-mod git vim ruby -y
	sudo yum install texinfo -y

	cd ~/.cache

	if [ ! -d ponysay ]
	then
		git clone https://github.com/erkin/ponysay.git
	fi
	cd ponysay
	sudo ./setup.py  install --freedom=partial

	cd ~
	touch ~/$FILE_CHECK
	cowsay "fin de Instalando cool things"
fi
