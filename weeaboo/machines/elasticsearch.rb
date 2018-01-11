Dir[ File.dirname(__FILE__) + "/base.rb" ].each { |file| require file }

class Elasticsearch < Base_centos
	def initialize( name='Elasticsearch' )
		super()
		@name = name
		@abstract = true
		@box = "base_centos_7"
		@scripts = [
			Python.new( "provision/copy_host.py" ),
			Python.new( "provision/repos/cp_all_repos.py" ),
			Python.new( "provision/stuff/install_java.py" ),
			Python.new( "provision/elasticsearch/install_elasticsearch.py" ),
			Python.new( "provision/elasticsearch/install_kibana.py" ),
			#Script.new( "provision/elasticsearch/start_elasticsearch.sh", args: [ @name ] ),
			#Script.new( "provision/elasticsearch/start_kibana.sh" ),
			#Script.new( "provision/elasticsearch/install_dashboards.sh" ),
			#Script.new( "provision/logstash/install_topbeat.sh" ),
			#Script.new( "provision/logstash/start_topbeat.sh", args: [ 'topbeat_elasticsearch.yml' ] ),
		]
	end
end

class Misuzu < Elasticsearch
	def initialize( name='Misuzu' )
		super( 'Misuzu' )
		@abstract = false
	end
end

class Pitou < Elasticsearch
	def initialize()
		super( 'Pitou' )
		@abstract = false
	end
end

class Sakura < Elasticsearch
	def initialize()
		super( 'Sakura' )
		@abstract = false
	end
end

class Rem < Elasticsearch
	def initialize()
		super( 'Rem' )
		@abstract = false
	end
end

class Rei < Elasticsearch
	def initialize()
		super( 'Rei' )
		@abstract = false
	end
end

class Ren < Elasticsearch
	def initialize()
		super( 'Ren' )
		@abstract = false
	end
end

class Sonico < Elasticsearch
	def initialize()
		super( 'Sonico' )
		@abstract = false
	end
end

class Tifa < Elasticsearch
	def initialize()
		super( 'Tifa' )
		@abstract = false
	end
end
