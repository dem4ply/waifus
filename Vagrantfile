# -*- mode: ruby -*-
# vi: set ft=ruby :

HOST_SHARE_FOLDER = "src"
GUEST_SHARE_FOLDER = "/home/vagrant/src"
GUEST_SHARE_FOLDER_PROVISION = "/home/vagrant/provision"

Vagrant.configure(2) do |config|

	#config.vm.box = "box-cutter/centos70"
	config.vm.box = "geerlingguy/centos7"

	config.vm.synced_folder HOST_SHARE_FOLDER, GUEST_SHARE_FOLDER, owner: "vagrant", group: "vagrant", create: true
	config.vm.synced_folder 'provision', GUEST_SHARE_FOLDER_PROVISION, owner: "vagrant", group: "vagrant", create: true

	# nginx
	config.vm.define "nginx", primary: true do |nginx|
		#nginx.vm.box = 'centos_cool'
		nginx.vm.host_name = "nginx"

		#nginx.vm.network "public_network", ip: "192.168.15.50"
		nginx.vm.network "public_network", bridge: "wlp2s0", ip: "192.168.1.150"

		nginx.vm.provider "virtualbox" do |vb|
			vb.name = "nginx"
			vb.memory = 512
			vb.cpus = 1
		end

		nginx.vm.provision :shell, path: "provision/install_python.sh"
		nginx.vm.provision :shell, path: "provision/install_cool.sh"
		nginx.vm.provision :shell, path: "provision/copy_hosts.sh"
		nginx.vm.provision :shell, path: "provision/nginx/install_nginx.sh"
		nginx.vm.provision :shell, path: "provision/nginx/start_nginx.sh"
	end

	# nodo de elasticserarch Sakura card captor
	config.vm.define "sakura" do |sakura|
		#sakura.vm.box = 'centos_cool'
		sakura.vm.host_name = "sakura"

		#sakura.vm.network "public_network", ip: "192.168.15.60"
		sakura.vm.network "public_network", bridge: "wlp2s0", ip: "192.168.1.160"

		sakura.vm.provider "virtualbox" do |vb|
			vb.name = "sakura"
			vb.memory = 1024
			vb.cpus = 1
		end
		sakura.vm.provision :shell, path: "provision/install_python.sh"
		sakura.vm.provision :shell, path: "provision/install_cool.sh"
		sakura.vm.provision :shell, path: "provision/copy_hosts.sh"
		sakura.vm.provision :shell, path: "provision/elasticsearch/install_elasticsearch.sh"
		sakura.vm.provision :shell, path: "provision/elasticsearch/start_elasticsearch.sh", args: "sakura"
	end

	config.vm.define "pitou" do |pitou|
		#pitou.vm.box = 'centos_cool'
		pitou.vm.host_name = "pitou"

		#pitou.vm.network "public_network", ip: "192.168.15.60"
		pitou.vm.network "public_network", bridge: "wlp2s0", ip: "192.168.1.161"

		pitou.vm.provider "virtualbox" do |vb|
			vb.name = "pitou"
			vb.memory = 1024
			vb.cpus = 1
		end
		pitou.vm.provision :shell, path: "provision/install_python.sh"
		pitou.vm.provision :shell, path: "provision/install_cool.sh"
		pitou.vm.provision :shell, path: "provision/copy_hosts.sh"
		pitou.vm.provision :shell, path: "provision/elasticsearch/install_elasticsearch.sh"
		pitou.vm.provision :shell, path: "provision/elasticsearch/start_elasticsearch.sh", args: "pitou"
		pitou.vm.provision :shell, path: "provision/elasticsearch/install_kibana.sh"
		pitou.vm.provision :shell, path: "provision/elasticsearch/start_kibana.sh"
	end

	config.vm.define "ren" do |ren|
		#ren.vm.box = 'centos_cool'
		ren.vm.host_name = "ren"

		#ren.vm.network "public_network", ip: "192.168.15.60"
		ren.vm.network "public_network", bridge: "wlp2s0", ip: "192.168.1.162"

		ren.vm.provider "virtualbox" do |vb|
			vb.name = "ren"
			vb.memory = 1024
			vb.cpus = 1
		end
		ren.vm.provision :shell, path: "provision/install_python.sh"
		ren.vm.provision :shell, path: "provision/install_cool.sh"
		ren.vm.provision :shell, path: "provision/copy_hosts.sh"
		ren.vm.provision :shell, path: "provision/elasticsearch/install_elasticsearch.sh"
		ren.vm.provision :shell, path: "provision/elasticsearch/start_elasticsearch.sh", args: "ren"
	end

	config.vm.define "misuzu" do |misuzu|
		#misuzu.vm.box = 'centos_cool'
		misuzu.vm.host_name = "misuzu"

		#misuzu.vm.network "public_network", ip: "192.168.15.60"
		misuzu.vm.network "public_network", bridge: "wlp2s0", ip: "192.168.1.163"

		misuzu.vm.provider "virtualbox" do |vb|
			vb.name = "misuzu"
			vb.memory = 1024
			vb.cpus = 1
		end
		misuzu.vm.provision :shell, path: "provision/install_python.sh"
		misuzu.vm.provision :shell, path: "provision/install_cool.sh"
		misuzu.vm.provision :shell, path: "provision/copy_hosts.sh"
		misuzu.vm.provision :shell, path: "provision/elasticsearch/install_elasticsearch.sh"
		misuzu.vm.provision :shell, path: "provision/elasticsearch/start_elasticsearch.sh", args: "misuzu"
	end
	#
	#
	# base
#	config.vm.define "centos_cool", primary: true do |centos_cool|
#		centos_cool.vm.host_name = "centos_cool"
#
#		#centos_cool.vm.network "public_network", ip: "192.168.15.50"
#		#centos_cool.vm.network "public_network", bridge: "wlp2s0", ip: "192.168.1.150"
#
#		centos_cool.vm.provider "virtualbox" do |vb|
#			vb.name = "centos_cool"
#			vb.memory = 512
#			vb.cpus = 1
#		end
#
#		centos_cool.vm.provision :shell, path: "provision/install_python.sh"
#		centos_cool.vm.provision :shell, path: "provision/install_cool.sh"
#	end
end
