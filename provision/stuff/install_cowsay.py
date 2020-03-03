#!/usr/bin/env python3
from chibi.config import basic_config
from chibi.file import Chibi_path
from chibi.net import download
from chibi_command.centos import Yum
from chibi_command.echo import echo, cowsay


basic_config()
file_check_path = Chibi_path( '~/provision_installed' )
file_check = file_check_path.open()

url_of_cowsay_rpm = (
    "http://www.melvilletheatre.com/articles/el7/"
    "cowsay-3.03-14.el7.centos.noarch.rpm"
)


version_to_check = (
    "cowsay with {url}\n".format( url=url_of_cowsay_rpm )
)

cache_directory = Chibi_path( '~/.cache/' )
full_path_cowsay_rpm = cache_directory + 'cowsay.rpm'


if __name__ == "__main__" and not version_to_check in file_check:
    echo( '===============================' )
    echo( 'iniciando instalacion de cowsay' )
    echo( '===============================' )

    if not full_path_cowsay_rpm.exists:
        download(
            url_of_cowsay_rpm, directory=cache_directory,
            file_name='cowsay.rpm' )
    else:
        echo.echo( "usando el cache para instalar cowsay" )

    Yum.local_install( full_path_cowsay_rpm )

    cowsay( 'finalizando instalacion de cowsay' )
    file_check.append( version_to_check )
