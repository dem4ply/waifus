FILE_CHECK=".install_rabbitmq"

if [ ! -f ~/$FILE_CHECK ]
then
	cowsay "Instalado rabbitmq"

	FOLDER_PROVISION="/home/vagrant/provision"

	if [ -f ~/.cache/rabbitmq.rpm ]
	then
		echo "using cache for install erlang"
	else
		rpm --import https://www.rabbitmq.com/rabbitmq-signing-key-public.asc
		wget --no-cookies --no-check-certificate \
			--progress=bar:force \
			-O /tmp/rabbitmq.rpm \
			"https://www.rabbitmq.com/releases/rabbitmq-server/v3.6.1/rabbitmq-server-3.6.1-1.noarch.rpm"
		mv /tmp/rabbitmq.rpm ~/.cache/
	fi

	yum localinstall -y ~/.cache/rabbitmq.rpm

	firewall-cmd --permanent --add-port=4369/tcp
	firewall-cmd --permanent --add-port=25672/tcp
	firewall-cmd --permanent --add-port=5671-5672/tcp
	firewall-cmd --permanent --add-port=15672/tcp
	firewall-cmd --permanent --add-port=61613-61614/tcp
	firewall-cmd --permanent --add-port=8883/tcp

	firewall-cmd --reload

	setsebool -P nis_enabled 1
	systemctl start rabbitmq-server
	systemctl enable rabbitmq-server

	touch ~/$FILE_CHECK
	cowsay "fin de instalacion de rabbitmq"
fi
