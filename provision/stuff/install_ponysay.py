#!/usr/bin/env python3
from chibi.command import git
from chibi_command.centos import Yum
from chibi_command import Command
from chibi_command.echo import cowsay
from chibi.file import Chibi_file, Chibi_path
from chibi.file.snippets import current_dir, cd


cache_dir = Chibi_path( '~/.cache' )
file_check_path = Chibi_path( '~/provision_installed' )
file_check = Chibi_file( file_check_path )


version_to_check = "ponysay\n".format( file=__file__, )


if __name__ == "__main__" and not version_to_check in file_check:
    cowsay( "Starting install for ponysay" )
    Yum.install( 'texinfo' )
    original_dir = current_dir()
    cd( cache_dir )
    ponysay_dir = cache_dir + 'ponysay'

    if not ponysay_dir.exists:
        git.clone( 'https://github.com/erkin/ponysay.git', ponysay_dir )

    cd( ponysay_dir )

    Command( 'python3' )( './setup.py', 'install', '--freedom=partial' )

    cd( original_dir )
    file_check.append( version_to_check )
