#!/usr/bin/env python3
from chibi.config import basic_config
from chibi.file import Chibi_path
from chibi_command.centos import Dnf
from chibi_command.echo import echo


basic_config()
file_check_path = Chibi_path( '~/provision_installed' )
file_check = file_check_path.open()

version_to_check = ( "epel-release\n" )


if __name__ == "__main__" and not version_to_check in file_check:
    echo( '=====================================' )
    echo( 'iniciando instalacion de epel-release' )
    echo( '=====================================' )

    Dnf.install( "epel-release" )
    file_check.append( version_to_check )

    echo( '===============================' )
    echo( 'termino de instalo epel release' )
    echo( '===============================' )
