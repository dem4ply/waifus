Dir[ File.dirname(__FILE__) + "/../machine.rb" ].each { |file|
	require file
}
Dir[ File.dirname(__FILE__) + "/../script.rb" ].each { |file|
	require file
}

class Base_centos < Machine
	def initialize()
		@name = 'base-centos-7'
		@ram = 512
		@cpus = 1
		@abstract = false
		@scripts = [
			Script.new( "provision/stuff/install_cowsay.sh" ),
			Script.new( "provision/copy_hosts.sh" ),
			Script.new( "provision/repos/cp_all.sh" ),
			Script.new( "provision/install_python.sh" ),
			Script.new( "provision/install_cool.sh" ),
			Script.new( "provision/install_htop.sh" ),
		]
	end
end
