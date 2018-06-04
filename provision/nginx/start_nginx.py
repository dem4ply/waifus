from chibi.file import mkdir, copy, ln, exists, ls, join
from chibi.command import systemctl
from chibi.command.echo import cowsay


FOLDER_PROVISION="/home/vagrant/provision/nginx/provision"

cowsay( "inicia de inicio de nginx" )

folders = (
    "/var/log/nginx", "/etc/nginx/sites_available",
    "/etc/nginx/sites_enabled" )

for folder in folders:
    mkdir( folder, verbose=True )

folders = ( 'conf.d', "sites_available" )

for folder in folders:
    nginx_folder = join( '/etc/nginx/', folder )
    provision_folder = join( FOLDER_PROVISION, folder )
    files = ls( provision_folder )
    for file in files:
        copy(
            join( provision_folder, file ), join( nginx_folder, file ),
            verbose=True )

copy(
    join( FOLDER_PROVISION, 'nginx.conf' ),
    join( '/etc/nginx/', 'nginx.conf' ), verbose=True )


ls()

if not exists( "/etc/nginx/sites_enabled/waifus.conf" ):
    ln(
        "/etc/nginx/sites_available/waifus.conf",
        "/etc/nginx/sites_enabled/waifus.conf" )
else:
    print( "el archivo de waifus existe" )

if not exists( "/etc/nginx/sites_enabled/kibana.conf" ):
    ln(
        "/etc/nginx/sites_available/kibana.conf",
        "/etc/nginx/sites_enabled/kibana.conf" )
else:
    print( "el archivo de kibana existe" )


systemctl.restart( "nginx" )


cowsay( "fin de inicio de nginx" )
