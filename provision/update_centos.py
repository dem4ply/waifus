#!/usr/bin/env python3
from chibi.file import Chibi_path
from chibi_command.centos import Yum
from chibi_command.echo import cowsay


file_check_path = Chibi_path( '~/provision_installed' )
file_check = file_check_path.open()


version_to_check = "{file}\n".format( file=__file__ )


if __name__ == "__main__" and not version_to_check in file_check:
    cowsay( "updating centos" )
    Yum.update()
    Yum.install( 'epel-release' )
    file_check.append( version_to_check )
    cowsay( "end of updating centos" )
