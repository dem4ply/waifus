#!/bin/bash
set -e
#set +v

echo "update global"
pip3 install --upgrade pip
pip3 install --upgrade python-hosts
pip3 install --upgrade chibi chibi-requests chibi_command chibi-donkey chibi-nginx

set +e
#set -v

#cd ~/python_lib/
#cowsay "iniciando actualizacion de bibliotecas locales de python"
#
#
#libs=$(ls -F | grep /)
#for lib in $libs;
#do
#	echo "updating $lib"
#	cd $lib
#	git pull
#	pip3 uninstall $lib
#	pip3 install ./
#	cd ..
#done
