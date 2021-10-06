Dir[ File.dirname(__FILE__) + "/base.rb" ].each { |file| require file }

class LXC < Base_centos
	def initialize()
		super
		@abstract = true
		@name = 'LXC'
		@box = "base_centos_7"
		@ram = 1024
		@scripts = [
			Script.new( "provision/update_python_lib.sh" ),
			Python.new( "provision/add_user.py",
				args: [ 'chibi' ] ),
			Python.new( "provision/copy_host.py" ),
			Python.new( "provision/repos/cp_all_repos.py" ),

			Python.new( "provision/lxc/install.py" ),
			Script.new( "provision/lxc/install_chibi_lxc.sh" ),
			Python.new( "provision/git_clone.py",
				args: [ 'https://github.com/dem4ply/waifus.git' ] ),
			Python.new( "provision/lxc/provision.py" ),
		]
	end
end

class Koko < LXC
	def initialize()
		super
		@abstract = false
		@name = 'Koko'
	end
end
