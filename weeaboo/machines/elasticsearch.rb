Dir[ File.dirname(__FILE__) + "/base.rb" ].each { |file| require file }

class Elasticsearch < Base_centos
	def initialize()
		super
		@name = 'Elasticsearch'
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
	def initialize()
		super
		@name = 'Misuzu'
		@abstract = false
	end
end

class Pitou < Elasticsearch
	def initialize()
		super
		@name = 'Pitou'
		@abstract = false
	end
end

class Sakura < Elasticsearch
	def initialize()
		super
		@name = 'Sakura'
		@abstract = false
	end
end

class Rem < Elasticsearch
	def initialize()
		super
		@name = 'Rem'
		@abstract = false
	end
end

class Rei < Elasticsearch
	def initialize()
		super
		@name = 'Rei'
		@abstract = false
	end
end

class Ren < Elasticsearch
	def initialize()
		super
		@name = 'Ren'
		@abstract = false
	end
end

class Sonico < Elasticsearch
	def initialize()
		super
		@name = 'Sonico'
		@abstract = false
	end
end

class Tifa < Elasticsearch
	def initialize()
		super
		@name = 'Tifa'
		@abstract = false
	end
end
