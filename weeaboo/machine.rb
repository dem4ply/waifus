class Machine
	attr_reader :name
	def initialize()
		@name = name
		@box = "base_centos_7"
		@hosts_names = []
	end

	def hosts()
		result = "#{@name}"
		@hosts_names.each { | name |
			result << " #{name}"
		}
		return result
	end

	def assing_ip( ip )
		@ip = ip
	end

	def make_config( config )
		#config.vm.box = "base_centos_7"
		#config.vm.box = @box
		config.vm.define @name, primary: true do | m |
			self.make_build( m )
		end
	end

	def make_build( machine )
		machine.vm.box = @box
		machine.vm.host_name = @name
		self.make_network( machine )
		machine.vm.provider "virtualbox" do |vb|
			self.make_provider( vb )
		end
		self.make_scripts( machine )
	end

	def make_network( machine )
		#machine.vm.network "public_network", ip: @ip
		#machine.vm.network "public_network", bridge: "wlp2s0", ip: @ip,
		#machine.vm.network "private_network", bridge: "wlp2s0", ip: @ip,
			#virtualbox__intnet: "mynetwork"
		machine.vm.network "private_network", ip: @ip
	end

	def make_provider( provider )
		provider.name = @name
		provider.memory = @ram
		provider.cpus = @cpus

	end

	def make_scripts( machine )
		@scripts.each{ | script |
			if script.instance_of? Script
				machine.vm.provision(
					:shell, path: script.path,
						args: script.args.join( ' ' ),
						keep_color: true )
			end

			if script.instance_of? Python
				machine.vm.provision(
					:shell, path: script.path,
						args: script.args.join( ' ' ),
						keep_color: true )
			end
		}
	end
end
