#!/usr/bin/env python3
from chibi.config import basic_config
from chibi.file import Chibi_path
from chibi_command.centos import Yum
from chibi_command.echo import cowsay
from chibi_command.nix import Systemctl


basic_config()
file_check_path = Chibi_path( '~/provision_installed' )
file_check = file_check_path.open()


version_to_check = "kibana\n"


if __name__ == "__main__" and version_to_check not in file_check:
    cowsay( "Starting install for kibana" )

    Yum.install( 'kibana' )

    file_check.append( version_to_check )
    cowsay( "Ending install for kibana" )
