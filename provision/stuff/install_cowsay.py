#!/usr/bin/env python3
from chibi.command import echo, yum
from chibi.file import Chibi_file
from chibi.file.snippets import inflate_dir, join, exists
from chibi.net import download


file_check_path = inflate_dir( '~/provision_installed' )
file_check = Chibi_file( file_check_path )

url_of_cowsay_rpm = (
    "http://www.melvilletheatre.com/articles/el7/"
    "cowsay-3.03-14.el7.centos.noarch.rpm"
)


version_to_check = (
    "cowsay with {url}\n".format( file=__file__, url=url_of_cowsay_rpm )
)

cache_directory = inflate_dir( '~/.cache/' )
full_path_cowsay_rpm = join( cache_directory, 'cowsay.rpm' )


if __name__ == "__main__" and not version_to_check in file_check:
    echo.echo( '===============================' )
    echo.echo( 'iniciando instalacion de cowsay' )
    echo.echo( '===============================' )

    if not exists( full_path_cowsay_rpm ):
        download( url_of_cowsay_rpm,
                  directory=cache_directory,
                  file_name='cowsay.rpm' )
    else:
        echo.echo( "usando el cache para instalar cowsay" )

    yum.local_install( full_path_cowsay_rpm )

    echo.cowsay( 'finalizando instalacion de cowsay' )
    file_check.append( version_to_check )
