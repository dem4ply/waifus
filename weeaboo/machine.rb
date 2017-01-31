class Machine
	attr_reader :name
	def initializer()
		@name = name
	end

	def assing_ip( ip )
		@ip = ip
	end

	def make_config( config )
		config.vm.define @name, primary: true do | m |
			self.make_build( m )
		end
	end

	def make_build( machine )
		machine.vm.host_name = @name
		self.make_network( machine )
		machine.vm.provider "virtualbox" do |vb|
			self.make_provider( vb )
		end
		self.make_scripts( machine )
	end

	def make_network( machine )
		#machine.vm.network "public_network", ip: @ip
		machine.vm.network "public_network", bridge: "wlp2s0", ip: @ip
	end

	def make_provider( provider )
		provider.name = @name
		provider.memory = @ram
		provider.cpus = @cpus
	end

	def make_scripts( machine )
		@scripts.each{ | script |
			machine.vm.provision(
				:shell, path: script.path, args: script.args.join( ' ' ) )
		}
	end
end
