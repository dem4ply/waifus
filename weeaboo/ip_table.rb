class Ip_table
	def initialize( ip_start )
		@ip_start = ip_start
		@current_ip = @ip_start
		@ip_uses = []

		@machine_table = {}

	end

	def add( name, ip: nil, comment: '' )
		if ip == nil
			self.increment_ip()
			ip = @current_ip
		end
		@machine_table[ name ] = ip
		return ip
	end

	def get_or_add( name, ip: nil, comment: '' )
		if @machine_table.has_key? name
			return @machine_table[ name ]
		end
		if ip == nil
			self.increment_ip()
			ip = @current_ip
		end
		@machine_table[ name ] = ip
	end

	def increment_ip()
		ip = @current_ip.split( '.' )
		ip[3] = ip[3].to_i + 1
		new_ip = ip.join( '.' )
		@current_ip = new_ip
		if @ip_uses.include?( @current_ip )
			self.increment_ip()
		end
	end

	def print()
		@machine_table.each { | machine, ip |
			machine = machine.ljust( 20 )
			puts "#{machine}\t#{ip}"
		}
	end

	def build_host_file( dir_file )
		file = ''
		file << '127.0.0.1'.ljust( 18 ) + "\tlocalhost\n"
		file << '::1'.ljust( 18 ) + "\tlocalhost\n"

		@machine_table.each { | machine, ip |
			#machine = machine.ljust( 20 )
			file << "#{ip.ljust(18)}\t#{machine}\n"
		}
		hosts_end = File.open( dir_file, "w")
		hosts_end.write( file )
		hosts_end.close()
	end

	def []( machine )
		return @machine_table[ machine ]
	end
end
