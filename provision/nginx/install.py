#!/usr/bin/env python3
from chibi.config import basic_config
from chibi.file import Chibi_path
from chibi_command.centos import Yum
from chibi_command.echo import cowsay
from chibi_command.nix import Systemctl


basic_config()
file_check_path = Chibi_path( '~/provision_installed' )
file_check = file_check_path.open()


version_to_check = "nginx\n".format( file=__file__, )


if __name__ == "__main__" and not version_to_check in file_check:
    cowsay( "iniciando instalacion de nginx" )
    Yum.install( "nginx" )
    Systemctl.enable( "nginx" )
    Systemctl.start( "nginx" )
    file_check.append( version_to_check )
    cowsay( "terminando instalacion de nginx" )
