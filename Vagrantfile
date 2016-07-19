# -*- mode: ruby -*-
# vi: set ft=ruby :

HOST_SHARE_FOLDER = "src"
GUEST_SHARE_FOLDER = "/home/vagrant/src"
GUEST_SHARE_FOLDER_PROVISION = "/home/vagrant/provision"

Vagrant.configure(2) do |config|

	config.vm.box = "box-cutter/centos70"

	config.vm.synced_folder HOST_SHARE_FOLDER, GUEST_SHARE_FOLDER, owner: "vagrant", group: "vagrant", create: true
	config.vm.synced_folder 'provision', GUEST_SHARE_FOLDER_PROVISION, owner: "vagrant", group: "vagrant", create: true

	# nginx
	config.vm.define "nginx", primary: true do |nginx|
		nginx.vm.host_name = "nginx"

		nginx.vm.network "public_network", ip: "192.168.15.50"

		nginx.vm.provider "virtualbox" do |vb|
			vb.name = "nginx"
			vb.memory = 512
			vb.cpus = 1
		end

		nginx.vm.provision :shell, path: "provision/copy_hosts.sh"
		nginx.vm.provision :shell, path: "provision/install_python.sh"
		nginx.vm.provision :shell, path: "provision/nginx/install_nginx.sh"
		nginx.vm.provision :shell, path: "provision/nginx/start_nginx.sh"
	end

	# nodo de elasticserarch Sakura card captor
	config.vm.define "sakura" do |sakura|
		sakura.vm.host_name = "sakura"

		sakura.vm.network "public_network", ip: "192.168.15.60"

		sakura.vm.provider "virtualbox" do |vb|
			vb.name = "sakura"
			vb.memory = 1024
			vb.cpus = 1
		end
		sakura.vm.provision :shell, path: "provision/hosts.sh"
		sakura.vm.provision :shell, path: "provision/elasticsearch/install_elasticsearch.sh"
		sakura.vm.provision :shell, path: "provision/elasticsearch/start_elasticsearch.sh"
	end
end
