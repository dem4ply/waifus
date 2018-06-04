from chibi.command import yum, systemctl
from chibi.command.echo import cowsay
from chibi.file import inflate_dir, Chibi_file


file_check_path = inflate_dir( '~/provision_installed' )
file_check = Chibi_file( file_check_path )


version_to_check = "{file}\n".format( file=__file__, )


if __name__ == "__main__" and not version_to_check in file_check:
    cowsay( "iniciando instalacion de nginx" )
    yum.install( "nginx" )
    systemctl.enable( "nginx" )
    systemctl.start( "nginx" )
    file_check.append( version_to_check )
    cowsay( "terminando instalacion de nginx" )
