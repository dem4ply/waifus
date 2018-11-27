Dir[ File.dirname(__FILE__) + "/base.rb" ].each { |file| require file }

class Redis < Base_centos
	def initialize()
		super
		@abstract = true
		@name = 'Redis'
		@box = "base_centos_7"
		@scripts = [
			Script.new( "provision/update_python_lib.sh" ),
			Python.new( "provision/copy_host.py" ),
			Python.new( "provision/repos/cp_all_repos.py" ),
			Python.new( "provision/redis/install.py" ),
			Python.new( "provision/redis/provision.py" ),
		]
	end
end

class Nanoha < Redis
	def initialize()
		super
		@abstract = false
		@name = 'Nanoha'
	end
end

class Fate < Redis
	def initialize()
		super
		@abstract = false
		@name = 'Fate'
	end
end
