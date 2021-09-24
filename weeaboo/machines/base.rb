Dir[ File.dirname(__FILE__) + "/../machine.rb" ].each { |file|
	require file
}
Dir[ File.dirname(__FILE__) + "/../script.rb" ].each { |file|
	require file
}

class Base_centos < Machine
	def initialize()
		super
		@name = 'base-centos-7'
		@ram = 400
		@cpus = 1
		@abstract = false
		@box = "centos/7"
		#@box = "base_centos_7"
		@scripts = [
			Script.new( "provision/install_python.sh" ),
			Python.new( "provision/stuff/install_cowsay.py" ),
			Script.new( "provision/update_python_lib.sh" ),
			Python.new( "provision/update_centos.py" ),
			Python.new( "provision/set_envars.py",
				args: [ "/vagrant/provision" ] ),
			Python.new( "provision/copy_host.py" ),
			Python.new( "provision/stuff/install_essential.py" ),
			Python.new( "provision/stuff/install_ponysay.py" ),
			Python.new( "provision/repos/cp_all_repos.py" ),
			Python.new( "provision/stuff/clean_box.py" ),
		]
	end
end
