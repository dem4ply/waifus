Dir[ File.dirname(__FILE__) + "/base.rb" ].each { |file| require file }

class Django < Base_centos
	def initialize()
		super
		@abstract = true
		@name = 'Django'
		@box = "base_centos_7"
		@ram = 512
		@scripts = [
			Script.new( "provision/update_python_lib.sh" ),
			Python.new( "provision/copy_host.py" ),
			Python.new( "provision/repos/cp_all_repos.py" ),
			Python.new( "provision/lxc/install.py" ),
			Python.new( "provision/django/provision.py" ),
		]
	end
end

class Shiro < Django
	def initialize()
		super
		@name = 'Shiro'
		@abstract = false
	end
end

class Shionji < Django
	def initialize()
		super
		@name = 'Shionji'
		@abstract = false
	end
end

class Victorique < Django
	def initialize()
		super
		@name = 'Victorique'
		@abstract = false
	end
end
