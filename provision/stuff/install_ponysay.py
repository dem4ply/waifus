#!/usr/bin/env python3
from chibi.config import basic_config
from chibi.file import Chibi_path
from chibi_command import Command
from chibi_command.centos import Yum
from chibi_command.echo import cowsay
from chibi_command.git import Git
from chibi_command.centos import Dnf
from chibi.file.snippets import cd


basic_config()
cache_dir = Chibi_path( '~/.cache' )
file_check_path = Chibi_path( '~/provision_installed' )
file_check = file_check_path.open()


version_to_check = "ponysay\n".format( file=__file__, )


if __name__ == "__main__" and not version_to_check in file_check:
    cowsay( "Starting install for ponysay" )
    Dnf.config_manager( 'powertools' )
    Dnf.install( 'texinfo' )
    cache_dir.mkdir()
    ponysay_dir = cache_dir + 'ponysay'

    if not ponysay_dir.exists:
        Git.clone( 'https://github.com/erkin/ponysay.git', ponysay_dir )

    cd( ponysay_dir )
    result = Command( 'python3' ).run(
        'setup.py', 'install', '--freedom=partial' )
    if not result:
        raise Exception( result.error )

    print( '\033[0m' )
    cowsay( 'termino de instalar ponysay' )
    file_check.append( version_to_check )
