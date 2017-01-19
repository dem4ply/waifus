Dir[ File.dirname(__FILE__) + "/base.rb" ].each { |file| require file }

class Elasticsearch < Base_centos
	def initialize( name='Elasticsearch' )
		super()
		@name = name
		@abstract = true
		@scripts = [
			Script.new( "provision/copy_hosts.sh" ),
			Script.new( "provision/repos/cp_all.sh" ),
			Script.new( "provision/stuff/install_java.sh" ),
			Script.new( "provision/elasticsearch/install_elasticsearch.sh" ),
			Script.new( "provision/elasticsearch/install_kibana.sh" ),
			Script.new( "provision/elasticsearch/start_elasticsearch.sh",
							args: [ @name ] ),
			Script.new( "provision/elasticsearch/start_kibana.sh" ),
			Script.new( "provision/elasticsearch/install_dashboards.sh" ),
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
