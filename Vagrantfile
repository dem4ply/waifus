# -*- mode: ruby -*-
# vi: set ft=ruby :

require 'yaml'

HOST_SHARE_FOLDER = "src"
GUEST_SHARE_FOLDER = "/home/vagrant/src"
GUEST_SHARE_FOLDER_PROVISION = "/home/vagrant/provision"

Angeloids = [ 'Ikaros', 'Nymph', 'Astraea', 'Caos' ]
Waifus = [ 'Sakura', 'Pitou', 'Misuzu', 'Ren', 'Sonico' ]
OS_tan = [ 'Yuu', 'Ai', 'Touko', 'Nanami' ]

Angeloids_config = YAML.load_file( 'angeloids.yml' )
Waifus_config = YAML.load_file( 'waifus.yml' )
Ostan_config = YAML.load_file( 'os_tan.yml' )

START_IP = "192.168.1.150"

natural_host = File.open("provision/natural_hosts", "r")
hosts = natural_host.read

Vagrant.configure(2) do |config|

	#config.vm.box = "box-cutter/centos70"
	config.vm.box = "geerlingguy/centos7"

	config.vm.synced_folder HOST_SHARE_FOLDER, GUEST_SHARE_FOLDER, owner: "vagrant", group: "vagrant", create: true
	config.vm.synced_folder 'provision', GUEST_SHARE_FOLDER_PROVISION, owner: "vagrant", group: "vagrant", create: true

	ip = START_IP.split( '.' )

	hosts << "#Angeloids\n"
	Angeloids.each{ |name|
		ip_machine = ip.join( '.' )
		config.vm.define name, primary: true do |m|
			m.vm.host_name = name
			m.vm.network "public_network", bridge: "wlp2s0", ip: ip_machine
			m.vm.provider "virtualbox" do |vb|
				vb.name = name
				vb.memory = Angeloids_config[ 'ram' ]
				vb.cpus = Angeloids_config[ 'cpus' ]
			end
		Angeloids_config[ 'provision' ].each { |provision|
			m.vm.provision :shell, path: provision[ 'path' ]
		}
	end
		hosts << ip_machine + "\t\t" + name + "\n"
		ip[3] = ip[3].to_i + 1
	}

	hosts << "#waifus\n"
	Waifus.each{ |name|
		ip_machine = ip.join( '.' )
		config.vm.define name, primary: true do |m|
			m.vm.host_name = name
			m.vm.network "public_network", bridge: "wlp2s0", ip: ip_machine
			m.vm.provider "virtualbox" do |vb|
				vb.name = name
				vb.memory = Waifus_config[ 'ram' ]
				vb.cpus = Waifus_config[ 'cpus' ]
			end
		Waifus_config[ 'provision' ].each { |provision|
			if provision.key?( 'args' )
				args = provision[ 'args' ].sub '{name}', name
				m.vm.provision :shell, path: provision[ 'path' ], args: args
			else
				m.vm.provision :shell, path: provision[ 'path' ]
			end
		}
	end
		hosts << ip_machine + "\t\t" + name + "\n"
		ip[3] = ip[3].to_i + 1
	}

	hosts << "#os_tan\n"
	OS_tan.each{ |name|
		ip_machine = ip.join( '.' )
		config.vm.define name, primary: true do |m|
			m.vm.host_name = name
			m.vm.network "public_network", bridge: "wlp2s0", ip: ip_machine
			m.vm.provider "virtualbox" do |vb|
				vb.name = name
				vb.memory = Ostan_config[ 'ram' ]
				vb.cpus = Ostan_config[ 'cpus' ]
			end
		Ostan_config[ 'provision' ].each { |provision|
			m.vm.provision :shell, path: provision[ 'path' ]
		}
	end
		hosts << ip_machine + "\t\t" + name + "\n"
		ip[3] = ip[3].to_i + 1
	}

	hosts_end = File.open("provision/hosts", "w")
	hosts_end.write( hosts )
	hosts_end.close()

end
