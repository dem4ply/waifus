Dir[ File.dirname(__FILE__) + "/base.rb" ].each { |file| require file }

class Magi < Base_centos
	def initialize()
		super
		@abstract = true
		@name = 'Magi'
		@scripts = [
			Script.new( "provision/copy_hosts.sh" ),
			Script.new( "provision/repos/cp_all.sh" ),
		]
	end
end

class Melchor < Magi
	def initialize()
		super
		@name = 'Melchor'
		@abstract = false
	end
end

class Baltasar < Magi
	def initialize()
		super
		@name = 'Baltasar'
		@abstract = false
	end
end

class Gaspar < Magi
	def initialize()
		super
		@name = 'Gaspar'
		@abstract = false
	end
end
