FILE_CHECK=".install_pacemaker"

if [ ! -f ~/$FILE_CHECK ]
then
	cowsay "Instalado pacemaker of $1"

	FOLDER_PROVISION="/home/vagrant/provision"
	sudo yum install -y pcs fence-agents-all
	sudo mkdir -p /var/log/cluster

	sudo cp -v $FOLDER_PROVISION/pacemaker/provision/corosync_$1.conf \
		/etc/corosync/corosync.conf

	cowsay "Si soy un servidor de verdad eres un imbecil"
	sudo cp -v $FOLDER_PROVISION/pacemaker/provision/authkey_$1 \
		/etc/corosync/authkey

	echo "asdf" | sudo passwd hacluster --stdin

	systemctl enable firewalld.service
	systemctl start firewalld.service
	firewall-cmd --permanent --add-service=high-availability
	firewall-cmd --reload

	systemctl start pcsd.service
	systemctl start pacemaker

	systemctl enable pcsd.service
	systemctl enable pacemaker

	pcs property set stonith-enabled=false
	pcs property set no-quorum-policy=ignore

	pcs resource create virtual_ip ocf:heartbeat:IPaddr2 ip=$2 cidr_netmask=32 op monitor interval=30s

	touch ~/$FILE_CHECK
	cowsay "fin de instalacion de pacemaker"
fi
