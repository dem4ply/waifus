Dir[ File.dirname(__FILE__) + "/base.rb" ].each { |file| require file }

class Scrapy < Base_centos
	def initialize()
		super
		@abstract = true
		@name = 'Scrapy'
		@scripts = [
			Script.new( "provision/copy_hosts.sh" ),
			Script.new( "provision/repos/cp_all.sh" ),
		]
	end
end

class Potato < Scrapy
	def initialize()
		super
		@name = 'Potato'
		@abstract = false
	end
end
