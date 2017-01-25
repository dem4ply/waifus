#!/bin/bash
FILE_CHECK=".install_mariadb"
if [ ! -f ~/$FILE_CHECK ]
then

	cowsay "Creando bases de datos"

	FOLDER_PROVISION="/home/vagrant/provision"

	mysql -u root -ppassword <<-EOF
CREATE DATABASE IF NOT EXISTS mad_scientist
EOF

	systemctl enable firewalld.service
	systemctl start firewalld.service

	firewall-cmd --add-port=3306/tcp 
	firewall-cmd --permanent --add-port=3306/tcp

	systemctl restart mariadb

	touch ~/$FILE_CHECK

	cowsay "Finalizado instalasion mariadb"
fi
