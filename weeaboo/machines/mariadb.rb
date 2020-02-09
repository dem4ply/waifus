Dir[ File.dirname(__FILE__) + "/base.rb" ].each { |file| require file }

class Maria < Base_centos
	def initialize()
		super
		@abstract = true
		@name = 'Maria'
		@box = "base_centos_7"
		@scripts = [
			Script.new( "provision/update_python_lib.sh" ),
			Python.new( "provision/copy_host.py" ),
			Python.new( "provision/repos/cp_all_repos.py" ),

			#Script.new( "provision/mariadb/install.sh" ),
			Python.new( "provision/mariadb/install.py" ),
			Python.new( "provision/mariadb/add_databases.py" ),
			#Script.new( "provision/mariadb/add_databases.sh" ),
		]
	end
end

class Chii < Maria
	def initialize()
		super
		@abstract = false
		@name = 'Chii'
	end
end

class Freya < Maria
	def initialize()
		super
		@abstract = false
		@name = 'Freya'
	end
end

class Sumomo < Maria
	def initialize()
		super
		@abstract = false
		@name = 'Sumomo'
	end
end
