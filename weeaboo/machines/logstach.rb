Dir[ File.dirname(__FILE__) + "/base.rb" ].each { |file| require file }

class Logstash < Base_centos
	def initialize()
		super
		@abstract = true
		@name = 'Logstash'
		@scripts = [
			Script.new( "provision/copy_hosts.sh" ),
			Script.new( "provision/repos/cp_all.sh" ),
			Script.new( "provision/stuff/install_java.sh" ),
			Script.new( "provision/logstash/install_logstash.sh" ),
			Script.new( "provision/logstash/start_logstash.sh" ),

			Script.new( "provision/logstash/install_topbeat.sh" ),
			Script.new( "provision/logstash/start_topbeat.sh",
							args: [ 'topbeat_logstash.yml' ] ),
		]
	end
end

class Tohru < Logstash
	def initialize()
		super
		@name = 'Tohru'
		@abstract = false
	end
end

class Kanna < Logstash
	def initialize()
		super
		@name = 'Kanna'
		@abstract = false
	end
end

class Elma < Logstash
	def initialize()
		super
		@name = 'Elma'
		@abstract = false
	end
end
