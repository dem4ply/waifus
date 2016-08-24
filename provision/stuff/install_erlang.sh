#!/bin/bash
FILE_CHECK=".install_erlang"
if [ ! -f ~/$FILE_CHECK ]
then
	cowsay "Instalando erlang"

	yum install -y gcc gcc-c++ glibc-devel make ncurses-devel openssl-devel autoconf java-1.8.0-openjdk-devel git wget wxBase.x86_64

	# download java
	if [ -f ~/.cache/erlang.rpm ]
	then
		echo "using cache for install erlang"
	else
		wget --no-cookies --no-check-certificate \
			--progress=bar:force \
			-O /tmp/erlang.rpm \
			"http://packages.erlang-solutions.com/erlang-solutions-1.0-1.noarch.rpm"
		mv /tmp/erlang.rpm ~/.cache/
	fi

	yum -y localinstall ~/.cache/erlang.rpm

	touch ~/$FILE_CHECK

	cowsay "fin de la instalacion de java"
fi
