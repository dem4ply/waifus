Dir[ File.dirname(__FILE__) + "/machines/*.rb" ].each { |file|
	require file
}

class Provision
	def initialize( config, ip_table )
		@config = config
		@ip_table = ip_table
		@machines = {
			base: [ Base_centos ],
			magi: [ Melchor, Baltasar, Gaspar, ],
			nginx: [ Ikaros, Astraea, Caos, Nymph ],
			elasticsearch: [ Misuzu, Pitou, Sakura, Rem, Rei, Ren, Sonico, Tifa, ],
			logstash: [ Ai, Nanami, Touko, Yuu, ],
			django: [ Shiro, Shionji, Victorique, ],
			scrapy: [ Potato ],
			rabbit: [ Cocoa, Chino, Rize ],
			maria: [ Chii, Sumomo, Freya ],
			postgresql: [ Cyborg_009, Cyborg_003 ],
		}
	end

	def create_machines()
		@machines.each { | owner, waifus |
			puts( owner )
			waifus.each{ | waifu |
				instance = waifu.new()
				ip = @ip_table.add( instance.name )
				instance.assing_ip( ip )
				instance.make_config( @config )
				name_waifu = "#{waifu}"
				puts( "\t#{name_waifu.ljust(10)} : #{ip}" )
			}
		}
	end
end
