#!/usr/bin/env python3
from chibi.command import echo, yum
from chibi.file import inflate_dir, Chibi_file, join, exists, current_dir, cd
from chibi.net import download
from chibi.command.echo import cowsay
from chibi.command import git, pip
from chibi.command import command


file_check_path = inflate_dir( '~/provision_installed' )
file_check = Chibi_file( file_check_path )


version_to_check = "{file}\n".format( file=__file__, )


if __name__ == "__main__" and not version_to_check in file_check:
    cowsay( "Starting install for java" )
    yum.install( 'java-1.8.0-openjdk.x86_64' )

    file_check.append( version_to_check )
    java_version = command( 'java', '-version', stdout='pipe' )
    cowsay(
        "Ending install for java, the version is\n{}".format( java_version ) )
