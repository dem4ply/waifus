#!/usr/bin/env python3
from chibi.config import basic_config
from chibi.file import Chibi_path
from chibi_command import Command
from chibi_command.centos import Yum
from chibi_command.echo import cowsay


basic_config()
file_check_path = Chibi_path( '~/provision_installed' )
file_check = file_check_path.open()


version_to_check = "java 1.8.0\n".format( file=__file__, )


if __name__ == "__main__" and not version_to_check in file_check:
    cowsay( "Starting install for java" )
    Yum.install( 'java-1.8.0-openjdk.x86_64' )

    file_check.append( version_to_check )
    java_version = Command( 'java', captive=True ).run( '-version' )
    if not java_version:
        raise Exception( "no se instalo java {vars( java_version ) }" )
    cowsay( f"Ending install for java, the version is\n{java_version.error}" )
