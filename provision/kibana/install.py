from chibi.command import yum
from chibi.command.echo import cowsay
from chibi.file import inflate_dir, Chibi_file
from chibi.command import command, systemctl


file_check_path = inflate_dir( '~/provision_installed' )
file_check = Chibi_file( file_check_path )


version_to_check = "{file}\n".format( file=__file__, )


if __name__ == "__main__" and not version_to_check in file_check:
    cowsay( "Starting install for kibana" )

    yum.install( 'kibana' )

    systemctl.enable( "kibana" )
    systemctl.start( "kibana" )

    file_check.append( version_to_check )
    cowsay( "Ending install for kibana" )
