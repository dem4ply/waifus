# -*- mode: ruby -*-
# vi: set ft=ruby :
#
require 'yaml'
require './weeaboo/ip_table.rb'
require './weeaboo/machine.rb'
require './weeaboo/provision.rb'

REL_DIR = File.dirname(__FILE__)
HOST_CACHE_SHARE_FOLDER = REL_DIR + "/" + "cache"
HOST_SHARE_FOLDER = REL_DIR + "/" + "src"
HOST_BACKUPS_SHARE_FOLDER = REL_DIR + "/" + "backups"
GUEST_SHARE_FOLDER = "/home/vagrant/src"
GUEST_SHARE_FOLDER_PROVISION = "/home/vagrant/provision"
GUEST_SHARE_FOLDER_CACHE = "/home/vagrant/.cache"
ROOT_GUEST_SHARE_FOLDER_CACHE = "/root/.cache"

BACKUPS_SHARE_FOLDER = "/home/vagrant/backups"


Vagrant.configure(2) do |config|

	#config.vm.box = "box-cutter/centos70"
	#config.vm.box = "insaneworks/centos"
	#config.vm.box = "geerlingguy/centos7"
	#config.vm.box = "centos_base_7"
	config.vm.box = "base_centos_7"


	#natural_host = File.open( REL_DIR + "/" + "provision/natural_hosts", "r")
	#hosts = natural_host.read

	#machines = YAML.load_file( REL_DIR + "/" +  'machines.yml' )


	config.vm.synced_folder(
		HOST_BACKUPS_SHARE_FOLDER, BACKUPS_SHARE_FOLDER, owner: "vagrant",
		group: "vagrant", create: true )

	config.vm.synced_folder(
		HOST_SHARE_FOLDER, GUEST_SHARE_FOLDER, owner: "vagrant",
		group: "vagrant", create: true )

	config.vm.synced_folder(
		'provision', GUEST_SHARE_FOLDER_PROVISION, owner: "vagrant",
		group: "vagrant", create: true )

	config.vm.synced_folder(
		HOST_CACHE_SHARE_FOLDER, GUEST_SHARE_FOLDER_CACHE, owner: "vagrant",
		group: "vagrant", create: true )

	config.vm.synced_folder(
		HOST_CACHE_SHARE_FOLDER, ROOT_GUEST_SHARE_FOLDER_CACHE,
		owner: "vagrant", group: "vagrant", create: true )


	start_ip = "192.168.2.100"
	ip_table = Ip_table.new( start_ip )

	if Vagrant.has_plugin?("vagrant-cachier")
		config.cache.scope = :box
		config.cache.synced_folder_opts = {
			#type: :nfs,
			mount_options: [ 'rw' ]
		}
	end
	config.vm.provision "shell",
		run: "always",
		inline: "
		sudo nmcli connection reload;
		sudo systemctl restart network.service;"
	provision = Provision.new( config, ip_table )

	provision.create_machines()

	#ip_table.print()
	ip_table.build_host_file( REL_DIR + "/" + "provision/hosts" )
end
