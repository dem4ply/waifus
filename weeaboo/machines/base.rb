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
		@box = "box-cutter/centos73"
		@scripts = [
			Script.new( "provision/install_python.sh" ),
			Python.new( "provision/update_python_lib.py" ),
			Python.new( "provision/update_centos.py" ),
			Python.new( "provision/stuff/install_cowsay.py" ),
			Python.new( "provision/copy_host.py" ),
			Python.new( "provision/stuff/install_essential.py" ),
			Python.new( "provision/stuff/install_ponysay.py" ),
			Python.new( "provision/stuff/install_htop.py" ),
			Python.new( "provision/repos/cp_all_repos.py" ),
		]
	end
end
