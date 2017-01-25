#!/bin/bash
FILE_CHECK=".install_mariadb"
if [ ! -f ~/$FILE_CHECK ]
then

	cowsay "Instalando mariadb"

	FOLDER_PROVISION="/home/vagrant/provision"

	yum install -y mariadb-server
	systemctl start mariadb
	systemctl enable mariadb

	mysql -u root <<-EOF
UPDATE mysql.user SET Password=PASSWORD('password') WHERE User='root';
DELETE FROM mysql.user WHERE User='root' AND Host NOT IN ('localhost', '127.0.0.1', '::1');
DELETE FROM mysql.user WHERE User='';
DELETE FROM mysql.db WHERE Db='test' OR Db='test_%';
CREATE USER 'dem4ply'@'%' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON *.* TO 'dem4ply'@'%';
FLUSH PRIVILEGES;
EOF

	systemctl enable firewalld.service
	systemctl start firewalld.service

	firewall-cmd --add-port=3306/tcp 
	firewall-cmd --permanent --add-port=3306/tcp

	systemctl restart mariadb

	touch ~/$FILE_CHECK

	cowsay "Finalizado instalasion mariadb"
fi
