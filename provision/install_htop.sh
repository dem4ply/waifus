#!/bin/bash

FILE_CHECK="install_htop"
if [ ! -f ~/$FILE_CHECK ]
then
	sudo yum install -y htop
fi
