Dir[ File.dirname(__FILE__) + "/base.rb" ].each { |file| require file }

class SQL_server < Base_centos
	def initialize()
		super
		@abstract = true
		@name = 'SQL server'
		@box = "base_centos_7"
		@ram = 2560
		@scripts = [
			Script.new( "provision/update_python_lib.sh" ),
			Python.new( "provision/copy_host.py" ),
			Python.new( "provision/repos/cp_all_repos.py" ),

			Python.new( "provision/sql_server/install.py" ),
		]
	end
end

class Misaka < SQL_server
	def initialize()
		super
		@abstract = false
		@name = 'Misaka'
	end
end
