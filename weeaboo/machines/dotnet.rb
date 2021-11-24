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
			Python.new( "provision/add_user.py",
				args: [ 'chibi' ] ),

			Python.new( "provision/copy_host.py" ),
			Python.new( "provision/repos/cp_all_repos.py" ),
			Python.new( "provision/dotnet/install.py" ),
			Script.new( "provision/dotnet/post_install.sh" ),
			Python.new( "provision/ssh/provision.py" ),

			Python.new( "provision/systemd/cp.py",
				args: [
						'dotnet/sigrha_clients.service',
					] ),

			# Added opportunities_service
			Python.new( "provision/systemd/cp.py",
				args: [
						'dotnet/sigrha_opportunities.service',
					] ),

			Python.new( "provision/git_clone.py",
				args: [
					'git@github.com:AptudeSiGRHA/clients_service.git',
					'main',
				] ),
			Python.new( "provision/git_clone.py",
				args: [
					'git@github.com:AptudeSiGRHA/opportunities_service.git',
					'main',
				] ),
			Python.new( "provision/git_clone.py",
				args: [
					'git@github.com:AptudeSiGRHA/ADLoginService.git',
					'main',
				] ),

			Script.new( "provision/dotnet/database_migration.sh",
				args: [
					'/home/chibi/projects/clients_service__main/API_Clients/',
					'/etc/systemd/system/sigrha_clients.env',
				] ),

				# Added migration for opportunities
				Script.new( "provision/dotnet/database_migration.sh",
					args: [
						'/home/chibi/projects/opportunities_service__main/Opportunities/',
						'/etc/systemd/system/sigrha_opportunities.env',
					] ),

			Python.new( "provision/systemd/systemd.py",
				args: [ 'enable', 'sigrha_clients.service' ] ),
			Python.new( "provision/systemd/systemd.py",
				args: [ 'start', 'sigrha_clients.service' ] ),

			# Added opportunities_service
			Python.new( "provision/systemd/systemd.py",
				args: [ 'enable', 'sigrha_opportunities.service' ] ),
			Python.new( "provision/systemd/systemd.py",
				args: [ 'start', 'sigrha_opportunities.service' ] ),
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
