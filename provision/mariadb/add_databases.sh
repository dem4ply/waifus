#!/bin/bash
FILE_CHECK=".install_mariadb"
if [ ! -f ~/$FILE_CHECK ]
then

	cowsay "Creando bases de datos"

	FOLDER_PROVISION="/home/vagrant/provision"

	mysql -u root -ppassword <<-EOF
CREATE DATABASE IF NOT EXISTS mad_scientist;
CREATE DATABASE IF NOT EXISTS notarius;
EOF

cowsay "Finalizado creacion de bases de datos"
