from chibi.command import yum, systemctl, command
from chibi.command.echo import cowsay
from chibi.file import inflate_dir, Chibi_file


file_check_path = inflate_dir( '~/provision_installed' )
file_check = Chibi_file( file_check_path )


version_to_check = "{file}\n".format( file=__file__, )


if __name__ == "__main__" and not version_to_check in file_check:
    cowsay( "instalado postgresql" )

    yum.install(
        "https://download.postgresql.org/pub/repos/yum/9.5/"
        "redhat/rhel-7-x86_64/pgdg-centos95-9.5-2.noarch.rpm" )

    yum.install(
        'postgresql95', 'postgresql95-server', 'postgresql95-libs',
        'postgresql95-contrib', 'postgresql95-devel' )
    yum.install( 'postgis2_95-client' )
    command( "/usr/pgsql-9.5/bin/postgresql95-setup", "initdb" )
    #command( "postgresql-setup", "initdb" )
    systemctl.start( "postgresql-9.5" )
    systemctl.enable( "postgresql-9.5" )

    cowsay( "termino de instalar postgresql" )

    file_check.append( version_to_check )
