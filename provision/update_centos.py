#!/usr/bin/env python3
from chibi.command import yum, echo
from chibi.file import Chibi_file
from chibi.file.snippets import inflate_dir


file_check_path = inflate_dir( '~/provision_installed' )
file_check = Chibi_file( file_check_path )


version_to_check = "{file}\n".format( file=__file__ )


if __name__ == "__main__" and not version_to_check in file_check:
    echo.cowsay( "updating centos" )
    yum.update()
    yum.install( 'epel-release' )
    file_check.append( version_to_check )
    echo.cowsay( "end of updating centos" )
