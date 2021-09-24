Dir[ File.dirname(__FILE__) + "/base.rb" ].each { |file| require file }

class Dot_net < Base_centos
	def initialize()
		super
		@abstract = true
		@name = 'Dot Net'
		@box = "base_centos_7"
		@ram = 1000
		@scripts = [
			Script.new( "provision/update_python_lib.sh" ),
			Python.new( "provision/copy_host.py" ),
			Python.new( "provision/repos/cp_all_repos.py" ),
		]
	end
end

class Mitsuha < Dot_net
	def initialize()
		super
		@abstract = false
		@name = 'Mitsuha'
	end
end