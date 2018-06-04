from chibi.command import yum, command, systemctl
from chibi.command.echo import cowsay
from chibi.file import inflate_dir, Chibi_file
from chibi.command import rpm


file_check_path = inflate_dir( '~/provision_installed' )
file_check = Chibi_file( file_check_path )


version_to_check = "{file}\n".format( file=__file__, )


if __name__ == "__main__" and not version_to_check in file_check:
    cowsay( "Starting install for elasticsearch" )

    rpm.rpm_import( 'https://artifacts.elastic.co/GPG-KEY-elasticsearch' )
    yum.install( 'elasticsearch' )

    systemctl.enable( 'elasticsearch.service' )
    systemctl.start( 'elasticsearch.service' )

    #command(
    #    '/usr/share/elasticsearch/bin/plugin', 'install',
    #    'royrusso/elasticsearch-HQ' )

    file_check.append( version_to_check )
    cowsay( "Ending install for elasticsearch" )
