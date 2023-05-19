#!/usr/bin/env python3
from chibi.config import basic_config
from chibi.file import Chibi_path
from chibi_command.centos import Dnf
from chibi_command.echo import cowsay


basic_config()
file_check_path = Chibi_path( '~/provision_installed' )
file_check = file_check_path.open()


version_to_check = "install_owcloud_dependencies\n".format( file=__file__, )


if __name__ == "__main__" and not version_to_check in file_check:
    cowsay( "iniciando instalacion de dependencias de owncloud de php" )
    Dnf.install(
        'php-gd', 'php-intl', 'php-pecl-apcu', 'php-process', 'php-zip' )
    file_check.append( version_to_check )
    cowsay( "terminando instalacion de dependencias de owncloud de php" )
