#!/usr/bin/env python3
from chibi.config import basic_config
from chibi.file import Chibi_path
from chibi_command import Command
from chibi_command.echo import cowsay
from chibi_command.nix import Yum, Systemctl


basic_config()
file_check_path = Chibi_path( '~/provision_installed' )
file_check = file_check_path.open()


version_to_check = "redis\n".format( file=__file__, )


if __name__ == "__main__" and not version_to_check in file_check:
    cowsay( "instalado redis" )

    Yum.install( 'redis' )
    Systemctl.start( "redis" ).run()
    Systemctl.enable( "redis" ).run()

    cowsay( "termino de instalar redis" )

    result = Command( 'redis-cli', 'ping', captive=True ).run()

    cowsay( "redis ping say: {}".format( result.result ) )

    file_check.append( version_to_check )
