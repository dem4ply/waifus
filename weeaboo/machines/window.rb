Dir[ File.dirname(__FILE__) + "/base.rb" ].each { |file| require file }


class Windows < Base_centos
	def initialize()
		super
		@abstract = true
		@name = 'Window'
	end
end


class Touko_madobe < Windows
	def initialize()
		super
		@name = 'Touko-Madobe'
		@abstract = false
	end
end


class Ai_madobe < Windows
	def initialize()
		super
		@name = 'Ai-Madobe'
		@abstract = false
	end
end


class Yuu_madobe < Windows
	def initialize()
		super
		@name = 'Yuu-Madobe'
		@abstract = false
	end
end


class Nanami_madobe < Windows
	def initialize()
		super
		@name = 'Nanami-Madobe'
		@abstract = false
	end
end
