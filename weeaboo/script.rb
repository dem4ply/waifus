class Script
	attr_reader :path, :args
	def initialize( path, args: [] )
		@path = path
		@args = args
	end
end
