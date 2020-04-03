#!/usr/bin/env python3
from chibi.config import basic_config
from chibi_command.echo import cowsay
from chibi_command.nix import Systemctl


basic_config()
provision_folder = (
    Chibi_path( os.environ[ 'PROVISION_PATH' ] ) + 'redis/provision' )

cowsay( "provisionado redis" )

redis_conf = provision_folder + "redis.conf"
redis_conf.copy( '/etc/redis.conf' )

Systemctl.restart( "redis" ).run()

cowsay( "termino de provisionado redis" )
