FILE_CHECK=".install_pacemaker"

rm ~/$FILE_CHECK

if [ ! -f ~/$FILE_CHECK ]
then
	cowsay "Instalado pacemaker of $1"

	FOLDER_PROVISION="/home/vagrant/provision"
	sudo yum install -y pcs fence-agents-all
	sudo mkdir -p /var/log/cluster

	"""
	sudo cp -v $FOLDER_PROVISION/pacemaker/provision/corosync_$1.conf \
		/etc/corosync/corosync.conf
	"""

	sudo cp -v $FOLDER_PROVISION/pacemaker/provision/authkey_$1 \
		/etc/corosync/authkey

	echo "asdf" | sudo passwd hacluster --stdin

	systemctl enable firewalld.service
	systemctl start firewalld.service
	firewall-cmd --permanent --add-service=high-availability
	firewall-cmd --reload

	systemctl start pcsd.service

	systemctl enable pcsd.service



	touch ~/$FILE_CHECK
	cowsay "fin de instalacion de pacemaker"
fi
