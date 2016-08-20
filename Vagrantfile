# -*- mode: ruby -*-
# vi: set ft=ruby :
#
require 'yaml'

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

	start_ip = "192.168.2.100"

	natural_host = File.open( REL_DIR + "/" + "provision/natural_hosts", "r")
	hosts = natural_host.read

	machines = YAML.load_file( REL_DIR + "/" +  'machines.yml' )


	config.vm.synced_folder HOST_BACKUPS_SHARE_FOLDER, BACKUPS_SHARE_FOLDER, owner: "vagrant", group: "vagrant", create: true
	config.vm.synced_folder HOST_SHARE_FOLDER, GUEST_SHARE_FOLDER, owner: "vagrant", group: "vagrant", create: true
	config.vm.synced_folder 'provision', GUEST_SHARE_FOLDER_PROVISION, owner: "vagrant", group: "vagrant", create: true
	config.vm.synced_folder HOST_CACHE_SHARE_FOLDER, GUEST_SHARE_FOLDER_CACHE, owner: "vagrant", group: "vagrant", create: true
	config.vm.synced_folder HOST_CACHE_SHARE_FOLDER, ROOT_GUEST_SHARE_FOLDER_CACHE, owner: "vagrant", group: "vagrant", create: true


	# nginx and django
	split_ip = start_ip.split( '.' )

	if Vagrant.has_plugin?("vagrant-cachier")
		config.cache.scope = :box
		config.cache.synced_folder_opts = {
			#type: :nfs,
			mount_options: [ 'rw' ]
		}
	end

	aux_machines = {}
	unique_config = {}
	for k, v in machines
		machines_names = v[ 'machines' ]
		machines_config = v[ 'config' ]

		hosts << "\# machines #{ k }\n"
		current_ip = split_ip.join( '.' )
		hosts << "#{ current_ip }\t\t#{ k } \#reserver for virtual_ip\n"
		split_ip[3] = split_ip[3].to_i + 1

		machines_names.each { |name|
			aux_machines[ name ] = machines_config
			unique_config[ name ] = machines_config.fetch( 'unique', {} ).fetch( name, {} )
			current_ip = split_ip.join( '.' )
			config.vm.define name, primary: true do |m|
				machines_config = aux_machines[ name ]
				m.vm.host_name = name
				m.vm.network "public_network", bridge: "wlp2s0", ip: current_ip
				m.vm.provider "virtualbox" do |vb|
					vb.name = name
					vb.memory = unique_config[ name ].fetch( 'ram', machines_config[ 'ram' ] )
					vb.cpus = unique_config[ name ].fetch( 'cpus', machines_config[ 'cpus' ] )
				end
				machines_config[ 'provisions' ].each { |provision|
					args = provision.fetch( 'args', '' ).sub '{name}', name
					path = REL_DIR + "/" + provision[ 'path' ]
					if ( args )
						m.vm.provision :shell, path: path, args: args
					else
						m.vm.provision :shell, path: path
					end
				}
			end
			#extra_host = v.fetch( 'extra_hosts', [] )
			hosts << "#{ current_ip }\t\t#{ name }\n"
			split_ip[3] = split_ip[3].to_i + 1
		}
	end

	hosts_end = File.open( REL_DIR + "/" + "provision/hosts", "w")
	hosts_end.write( hosts )
	hosts_end.close()

end
