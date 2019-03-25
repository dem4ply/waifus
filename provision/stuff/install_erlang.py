#!/usr/bin/env python3
from chibi.command import yum, rpm
from chibi.command.echo import cowsay
from chibi.file import Chibi_file
from chibi.file.snippets import inflate_dir
from chibi.net import download


file_check_path = inflate_dir( '~/provision_installed' )
file_check = Chibi_file( file_check_path )


version_to_check = "erlang\n".format( file=__file__, )


if __name__ == "__main__" and not version_to_check in file_check:
    cowsay( "instalando erlang" )
    yum.install(
        'gcc', 'gcc-c++', 'glibc-devel', 'make', 'ncurses-devel',
        'openssl-devel', 'autoconf', 'java-1.8.0-openjdk-devel', 'git',
        'wget', 'wxBase.x86_64' )

    download(
        "http://packages.erlang-solutions.com/"
        "erlang-solutions-1.0-1.noarch.rpm",
        directory='/tmp', file_name='erlang.rpm' )

    rpm.rpm( '-Uvh', '/tmp/erlang.rpm' )
    yum.install( 'erlang' )

    file_check.append( version_to_check )

    cowsay( " termino de instalar erlang" )
