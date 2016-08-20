#!/bin/bash
FILE_CHECK=".install_cowsay"
if [ ! -f ~/$FILE_CHECK ]
then
	echo "================="
	echo "Instalando cowsay"
	echo "================="

	if [ -f ~/.cache/cowsay.rpm ]
	then
		echo "using cache for install cowsay"
	else
		wget --progress=bar:force \
			-O ~/.cache/cowsay.rpm \
			"http://www.melvilletheatre.com/articles/el7/cowsay-3.03-14.el7.centos.noarch.rpm"
	fi

	sudo yum -y localinstall ~/.cache/cowsay.rpm

	cowsay "fin de la instalacion de cowsay"

	touch ~/$FILE_CHECK
fi
