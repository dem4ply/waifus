Dir[ File.dirname(__FILE__) + "/base.rb" ].each { |file| require file }

class Nginx < Base_centos
	def initialize()
		super
		@abstract = true
		@name = 'Nginx'
		@box = "base_centos_7"
		@ram = 512
		@scripts = [
			Script.new( "provision/update_python_lib.sh" ),
			Python.new( "provision/copy_host.py" ),
			Python.new( "provision/repos/cp_all_repos.py" ),

			Python.new( "provision/nginx/install.py" ),
			Python.new( "provision/nginx/start.py" ),
			#Script.new( "provision/logstash/install_filebeat.sh" ),
			#Script.new( "provision/logstash/install_topbeat.sh" ),
			#Script.new( "provision/logstash/install_packetbeat.sh" ),
			#Script.new( "provision/logstash/start_filebeat.sh",
			#				args: [ 'filebeat_nginx.yml' ] ),
			#Script.new( "provision/logstash/start_topbeat.sh",
			#				args: [ 'topbeat_nginx.yml' ] ),
			#Script.new( "provision/logstash/start_packetbeat.sh",
			#				args: [ 'packetbeat_nginx.yml' ] ),
		]
	end
end

class Ikaros < Nginx
	def initialize()
		super
		@abstract = false
		@name = 'Ikaros'
		@hosts_names = [
			'kibana', 'waifus', 'sigrha.com.mx',
			'api.sigrha.client.aptude.com' ]
	end
end

class Astraea < Nginx
	def initialize()
		super
		@abstract = false
		@name = 'Astraea'
	end
end

class Caos < Nginx
	def initialize()
		super
		@abstract = false
		@name = 'Caos'
	end
end

class Nymph < Nginx 
	def initialize()
		super
		@abstract = false
		@name = 'Nymph'
	end
end
