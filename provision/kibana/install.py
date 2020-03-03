#!/usr/bin/env python3
from chibi.file import Chibi_path
from chibi_command.centos import Yum
from chibi_command.echo import cowsay
from chibi_command.nix import Systemctl


file_check_path = Chibi_path( '~/provision_installed' )
file_check = file_check_path.open()


version_to_check = "kibana\n".format( file=__file__, )


if __name__ == "__main__" and not version_to_check in file_check:
    cowsay( "Starting install for kibana" )

    Yum.install( 'kibana' )

    Systemctl.enable( "kibana" )
    Systemctl.start( "kibana" )

    file_check.append( version_to_check )
    cowsay( "Ending install for kibana" )
