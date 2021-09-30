#!/bin/bash
FILE_CHECK=".nodejs14"

if [ ! -f ~/$FILE_CHECK ]
then
	cowsay "instalando nodejs 14"
	curl -sL https://rpm.nodesource.com/setup_14.x | sudo -E bash -
	yum -y install nodejs
	node -v | cowsay
	npm -v | cowsay
	touch ~/$FILE_CHECK
	cowsay "termino de instalando nodejs 14"
fi
