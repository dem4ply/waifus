#!/bin/bash
FILE_CHECK="install_java"
if [ ! -f ~/$FILE_CHECK ]
then
	echo "Instalando Java" | ponysay
	sudo yum update -y
	sudo rpm -iUvh http://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-release-7-5.noarch.rpm

	sudo yum groupinstall "Development Tools" -y

	# download java
	if [ -f ~/.cache/java.rpm ]
	then
		echo "using cache for install java"
	else
		wget --no-cookies --no-check-certificate -q \
			-O /tmp/java.rpm \
			--header "Cookie: gpw_e24=http%3A%2F%2Fwww.oracle.com%2F; oraclelicense=accept-securebackup-cookie"\
			"http://download.oracle.com/otn-pub/java/jdk/8u73-b02/jdk-8u73-linux-x64.rpm"
		mv /tmp/jave.rpm ~/.cache/
	fi

	sudo yum -y localinstall ~/.cache/java.rpm
	touch ~/$FILE_CHECK

	echo "fin de la instalacion de jave" | ponysay
fi
