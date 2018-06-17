Dir[ File.dirname(__FILE__) + "/base.rb" ].each { |file| require file }

class Postgresql < Base_centos
	def initialize()
		super
		@abstract = true
		@name = 'Postgresql'
		@box = "base_centos_7"
		@scripts = [
			Python.new( "provision/update_python_lib.py" ),
			Python.new( "provision/copy_host.py" ),
			Python.new( "provision/repos/cp_all_repos.py" ),
			Python.new( "provision/postgresql/install.py" ),
			Python.new( "provision/postgresql/provision.py" ),
		]
	end
end

class Cyborg_009 < Postgresql
	def initialize()
		super
		@abstract = false
		@name = 'Cyborg.009'
	end
end

class Cyborg_003 < Postgresql
	def initialize()
		super
		@abstract = false
		@name = 'Cyborg.003'
	end
end
