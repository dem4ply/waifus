#!/bin/bash
set -e

cowsay "update global"
pip3 install --upgrade pip
pip3 install --upgrade python-hosts
pip3 install --upgrade chibi
pip3 install --upgrade chibi-requests
pip3 install --upgrade chibi_command

set +e

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
