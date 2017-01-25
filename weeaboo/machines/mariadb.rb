Dir[ File.dirname(__FILE__) + "/base.rb" ].each { |file| require file }

class Maria < Base_centos
	def initialize()
		super
		@abstract = true
		@name = 'Maria'
		@scripts = [
			Script.new( "provision/copy_hosts.sh" ),
			Script.new( "provision/repos/cp_all.sh" ),
			Script.new( "provision/mariadb/install.sh" ),
		]
	end
end

class Chii < Maria
	def initialize()
		super
		@abstract = false
		@name = 'Chii'
	end
end

class Freya < Maria
	def initialize()
		super
		@abstract = false
		@name = 'Freya'
	end
end

class Sumomo < Maria
	def initialize()
		super
		@abstract = false
		@name = 'Sumomo'
	end
end
