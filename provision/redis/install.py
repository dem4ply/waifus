#!/usr/bin/env python3
from chibi.config import basic_config
from chibi.command import yum, systemctl, command
from chibi.command.echo import cowsay
from chibi.file.snippets import inflate_dir
from chibi.file import Chibi_file


basic_config()
file_check_path = inflate_dir( '~/provision_installed' )
file_check = Chibi_file( file_check_path )


version_to_check = "redis\n".format( file=__file__, )


if __name__ == "__main__" and not version_to_check in file_check:
    cowsay( "instalado redis" )

    yum.install( 'redis' )
    systemctl.start( "redis" )
    systemctl.enable( "redis" )

    cowsay( "termino de instalar redis" )

    result, error, return_code = command( 'redis-cli', 'ping', stdout='pipe' )

    cowsay( "redis ping say: {}".format( result ) )

    file_check.append( version_to_check )
