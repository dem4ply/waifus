#!/usr/bin/env python3
from chibi.config import basic_config
from chibi.file import Chibi_path
from chibi_command import Command
from chibi_command.centos import Systemctl
from chibi_command.echo import cowsay
from chibi_command.nix import Yum


basic_config()
file_check_path = Chibi_path( '~/provision_installed' )
file_check = file_check_path.open()


version_to_check = "postgresql install\n".format( file=__file__, )


if __name__ == "__main__" and not version_to_check in file_check:
    cowsay( "instalado postgresql" )

    Yum.install(
        "https://download.postgresql.org/pub/repos/yum/9.6/"
        "redhat/rhel-7-x86_64/pgdg-centos96-9.6-3.noarch.rpm" ).run()

    Yum.install(
        'postgresql96', 'postgresql96-server', 'postgresql96-libs',
        'postgresql96-contrib', 'postgresql96-devel' ).run()
    Yum.install( 'postgis2_96-client' ).run()
    Command( "/usr/pgsql-9.6/bin/postgresql96-setup", "initdb" ).run()
    #command( "postgresql-setup", "initdb" )
    Systemctl.start( "postgresql-9.6" ).run()
    Systemctl.enable( "postgresql-9.6" ).run()


    cowsay( "termino de instalar postgresql" )

    file_check.append( version_to_check )
