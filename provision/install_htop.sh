#!/bin/bash

FILE_CHECK="install_htop"
if [ ! -f ~/$FILE_CHECK ]
then
	cowsay "install htop"
	sudo yum install -y htop
	cowsay "end install htop"
fi
