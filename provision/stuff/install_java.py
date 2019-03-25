#!/usr/bin/env python3
from chibi.command import yum, command
from chibi.command.echo import cowsay
from chibi.file import Chibi_file
from chibi.file.snippets import inflate_dir


file_check_path = inflate_dir( '~/provision_installed' )
file_check = Chibi_file( file_check_path )


version_to_check = "java 1.8.0\n".format( file=__file__, )


if __name__ == "__main__" and not version_to_check in file_check:
    cowsay( "Starting install for java" )
    yum.install( 'java-1.8.0-openjdk.x86_64' )

    file_check.append( version_to_check )
    java_version = command( 'java', '-version', stdout='pipe' )
    cowsay(
        "Ending install for java, the version is\n{}".format( java_version ) )
