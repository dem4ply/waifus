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
		]
	end
end

class Ai < Logstash
	def initialize()
		super
		@name = 'Ai'
		@abstract = false
	end
end

class Nanami < Logstash
	def initialize()
		super
		@name = 'Nanami'
		@abstract = false
	end
end

class Touko < Logstash
	def initialize()
		super
		@name = 'Touko'
		@abstract = false
	end
end

class Yuu < Logstash
	def initialize()
		super
		@name = 'Yuu'
		@abstract = false
	end
end
