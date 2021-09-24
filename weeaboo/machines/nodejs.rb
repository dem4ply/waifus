Dir[ File.dirname(__FILE__) + "/base.rb" ].each { |file| require file }

class Nodejs < Base_centos
	def initialize()
		super
		@abstract = true
		@name = 'Nginx'
		@box = "base_centos_7"
		@ram = 512
		@scripts = [
			Script.new( "provision/update_python_lib.sh" ),
			Python.new( "provision/copy_host.py" ),
			Python.new( "provision/repos/cp_all_repos.py" ),
			Script.new( "provision/nodejs/install.sh" ),
		]
	end
end

class Asuka < Nodejs
	def initialize()
		super
		@abstract = false
		@name = 'Asuka'
	end
end
