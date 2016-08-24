#!/bin/bash
FILE_CHECK=".install_elixir"
rm ~/$FILE_CHECK
if [ ! -f ~/$FILE_CHECK ]
then
	FOLDER_PROVISION="/home/vagrant/provision"
	cowsay "Instalando elixir"

	cd ~/.cache/
	if [ -d ~/.cache/elixir ]
	then
		echo "using cache for install elixir"
	else
		git clone https://github.com/elixir-lang/elixir.git
	fi

	cd elixir
	make clean test
	export PATH="$PATH:/root/elixir/bin"

	cp -v $FOLDER_PROVISION/stuff/export_elixir.sh /etc/profile.d/elixir_expor.sh

	touch ~/$FILE_CHECK

	cowsay "fin de la instalacion de java"
fi
