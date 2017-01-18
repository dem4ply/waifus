Dir[ File.dirname(__FILE__) + "/base.rb" ].each { |file| require file }

class Django < Base_centos
	def initialize()
		super
		@abstract = true
		@name = 'Djano'
		@scripts = [
			Script.new( "provision/copy_hosts.sh" ),
			Script.new( "provision/repos/cp_all.sh" ),
		]
	end
end

class Shiro < Django
	def initialize()
		super
		@name = 'Shiro'
		@abstract = false
	end
end

class Shionji < Django
	def initialize()
		super
		@name = 'Shionji'
		@abstract = false
	end
end

class Victorique < Django
	def initialize()
		super
		@name = 'Victorique'
		@abstract = false
	end
end
