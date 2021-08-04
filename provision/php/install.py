#!/usr/bin/env python3
from chibi.config import basic_config
from chibi.file import Chibi_path
from chibi_command.centos import Yum
from chibi_command.echo import cowsay
from chibi_command.rpm import RPM


basic_config()
file_check_path = Chibi_path( '~/provision_installed' )
file_check = file_check_path.open()


version_to_check = "php5\n".format( file=__file__, )


if __name__ == "__main__":
    cowsay( "iniciando instalacion de php" )
    RPM(
        '-Uvh',
        'https://mirror.webtatic.com/yum/el7/webtatic-release.rpm' ).run()
    Yum.install(
        'php70w-fpm', 'php70w-cli', 'php70w-gd', 'php70w-mcrypt',
        'php70w-mysql', 'php70w-pear', 'php70w-xml', 'php70w-mbstring',
        'php70w-pdo', 'php70w-json' )
    file_check.append( version_to_check )
    cowsay( "terminando instalacion de php" )
