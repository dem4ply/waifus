#!/usr/bin/env python3
from chibi.command import echo, yum
from chibi.file import inflate_dir, Chibi_file, join, exists, current_dir, cd
from chibi.net import download
from chibi.command.echo import cowsay
from chibi.command import git, pip
from chibi.command import command


cache_dir = inflate_dir( '~/.cache' )
file_check_path = inflate_dir( '~/provision_installed' )
file_check = Chibi_file( file_check_path )


version_to_check = "{file}\n".format( file=__file__, )


if __name__ == "__main__" and not version_to_check in file_check:
    cowsay( "Starting install for ponysay" )
    yum.install( 'texinfo' )
    original_dir = current_dir()
    cd( cache_dir )
    ponysay_dir = join( cache_dir, 'ponysay' )

    if not exists( ponysay_dir ):
        git.clone( 'https://github.com/erkin/ponysay.git', ponysay_dir )

    cd( ponysay_dir )

    command( 'python3', './setup.py', 'install', '--freedom=partial' )

    cd( original_dir )
    file_check.append( version_to_check )
