#!/usr/bin/env python3
from chibi.config import basic_config
from chibi.file import Chibi_file
from chibi.file.snippets import inflate_dir
from chibi_command.centos import Yum
from chibi_command.echo import cowsay
from chibi_command.rpm import RPM
from chibi_requests import Chibi_url


basic_config()
file_check_path = inflate_dir( '~/provision_installed' )
file_check = Chibi_file( file_check_path )


version_to_check = "erlang\n".format( file=__file__, )


if __name__ == "__main__" and not version_to_check in file_check:
    cowsay( "instalando erlang" )
    yum.install(
        'gcc', 'gcc-c++', 'glibc-devel', 'make', 'ncurses-devel',
        'openssl-devel', 'autoconf', 'java-1.8.0-openjdk-devel', 'git',
        'wget', 'wxBase.x86_64' )

    erlang_url = Chibi_url(
        "http://packages.erlang-solutions.com/"
        "erlang-solutions-1.0-1.noarch.rpm" )
    erlang_rpm = erlang_url.download( path='/tmp' )

    RPM( '-Uvh' ).run( erlang_rpm )

    Yum.install( 'erlang' ).run()

    file_check.append( version_to_check )

    cowsay( " termino de instalar erlang" )
