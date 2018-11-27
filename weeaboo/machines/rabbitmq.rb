Dir[ File.dirname(__FILE__) + "/base.rb" ].each { |file| require file }

class Rabbitmq < Base_centos
	def initialize()
		super
		@abstract = true
		@name = 'rabbitmq'
		@box = "base_centos_7"
		@scripts = [
			Script.new( "provision/update_python_lib.sh" ),
			Python.new( "provision/copy_host.py" ),
			Python.new( "provision/repos/cp_all_repos.py" ),
			#Python.new( "provision/stuff/install_erlang.py" ),
			Python.new( "provision/rabbitmq/install.py" ),
			Python.new( "provision/rabbitmq/add_user.py" ),
			Python.new( "provision/rabbitmq/users/turn_profile.py" ),
			#Script.new( "provision/stuff/install_elixir.sh" ),
			#Script.new( "provision/rabbitmq/install_rabbitmq.sh" ),
			#Script.new( "provision/rabbitmq/add_user.sh" ),
			#Script.new( "provision/rabbitmq/users/goblins.sh" ),
			#Script.new( "provision/rabbitmq/users/pf_api.sh" ),
			#Script.new( "provision/rabbitmq/users/mad_hookshot.sh" ),
			#Script.new( "provision/rabbitmq/users/product_feed.sh" ),
			#Script.new( "provision/rabbitmq/users/madshopify.sh" ),
			#Script.new( "provision/rabbitmq/users/mad_message.sh" ),
		]
	end
end

class Cocoa < Rabbitmq
	def initialize()
		super
		@name = 'Cocoa'
		@abstract = false
	end
end

class Chino < Rabbitmq
	def initialize()
		super
		@name = 'Chino'
		@abstract = false
	end
end

class Rize < Rabbitmq
	def initialize()
		super
		@name = 'Rize'
		@abstract = false
	end
end
