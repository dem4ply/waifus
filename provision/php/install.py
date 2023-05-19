#!/usr/bin/env python3
from chibi.config import basic_config
from chibi.file import Chibi_path
from chibi_command.centos import Dnf
from chibi_command.echo import cowsay
from chibi_command.rpm import RPM


basic_config()
file_check_path = Chibi_path( '~/provision_installed' )
file_check = file_check_path.open()


version_to_check = "php\n".format( file=__file__, )


if __name__ == "__main__":
    cowsay( "iniciando instalacion de php" )
    Dnf().run( 'module', 'enable', 'php:7.4' )
    Dnf.install( 'php' )
    file_check.append( version_to_check )
    cowsay( "terminando instalacion de php" )
