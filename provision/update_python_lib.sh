#!/bin/bash
set -e
#set +v

echo "update global"
pip3 install --upgrade pip
pip3 install --upgrade python-hosts Jinja2
pip3 install --upgrade chibi chibi-requests chibi_command
pip3 install --upgrade chibi-donkey chibi-nginx chibi_git

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
