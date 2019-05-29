#!/usr/bin/env python3
from chibi.command import yum, systemctl, command
from chibi.command.echo import cowsay
from chibi.file import Chibi_file
from chibi.file.snippets import inflate_dir


file_check_path = inflate_dir( '~/provision_installed' )
file_check = Chibi_file( file_check_path )


version_to_check = "postgresql install\n".format( file=__file__, )


if __name__ == "__main__" and not version_to_check in file_check:
    cowsay( "instalado postgresql" )

    yum.install(
        "https://download.postgresql.org/pub/repos/yum/9.6/"
        "redhat/rhel-7-x86_64/pgdg-centos96-9.6-3.noarch.rpm" )

    yum.install(
        'postgresql96', 'postgresql96-server', 'postgresql96-libs',
        'postgresql96-contrib', 'postgresql96-devel' )
    yum.install( 'postgis2_96-client' )
    command( "/usr/pgsql-9.6/bin/postgresql96-setup", "initdb" )
    #command( "postgresql-setup", "initdb" )
    systemctl.start( "postgresql-9.6" )
    systemctl.enable( "postgresql-9.6" )


    cowsay( "termino de instalar postgresql" )

    file_check.append( version_to_check )
