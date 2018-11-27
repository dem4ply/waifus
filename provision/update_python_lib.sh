#!/bin/bash

cowsay "update gloabal"
pip3.7 install --upgrade chibi

cd ~/python_lib/
cowsay "iniciando actualizacion de bibliotecas locales de python"


libs=$(ls -F | grep /)
for lib in $libs;
do
	echo "updating $lib"
	cd $lib
	git pull
	pip3 uninstall $lib
	pip3 install ./
	cd ..
done
