Dir[ File.dirname(__FILE__) + "/base.rb" ].each { |file| require file }

class Nodejs < Base_centos
	def initialize()
		super
		@abstract = true
		@name = 'Nginx'
		@box = "base_centos_7"
		@ram = 1024
		@scripts = [
			Script.new( "provision/update_python_lib.sh" ),
			Python.new( "provision/add_user.py",
				args: [ 'chibi' ] ),
			Python.new( "provision/copy_host.py" ),
			Python.new( "provision/repos/cp_all_repos.py" ),
			Script.new( "provision/nodejs/install.sh" ),
			Python.new( "provision/ssh/provision.py" ),
			Python.new( "provision/git_clone.py",
				args: [ 'git@github.com:AptudeSiGRHA/sigrha-react.git' ] ),
			Script.new( "provision/nodejs/provison_repo.sh",
				args: [ '/home/chibi/projects/sigrha-react' ] ),

			Python.new( "provision/systemd/cp.py",
				args: [ 'nodejs/sigrha_react.service' ] ),
			Python.new( "provision/systemd/systemd.py",
				args: [ 'enable', 'sigrha_react.service' ] ),
			Python.new( "provision/systemd/systemd.py",
				args: [ 'start', 'sigrha_react.service' ] ),
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
