#!/usr/bin/env python3
from chibi.command import systemctl, command
from chibi.command.echo import cowsay
from chibi.file.snippets import copy, ln, exists, ls, join
from chibi.file import Chibi_file, Chibi_path
from chibi.net.hostname import get_hostname


FOLDER_PROVISION= Chibi_path( "/vagrant/provision/nginx/provision" )


cowsay( "inicia de inicio de nginx" )

command( 'setsebool', '-P', 'httpd_can_network_connect', '1', )

folders = (
    "/var/log/nginx", "/etc/nginx/sites_available",
    "/etc/nginx/sites_enabled" )

for folder in folders:
    Chibi_path( folder ).mkdir( verbose=True )

folders = ( 'conf.d', "sites_available" )

for folder in folders:
    nginx_folder = Chibi_path( '/etc/nginx/' ) + folder
    provision_folder = FOLDER_PROVISION + folder
    provision_folder.copy( nginx_folder )

copy(
    join( FOLDER_PROVISION, 'nginx.conf' ),
    join( '/etc/nginx/', 'nginx.conf' ), verbose=True )


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


if not exists( "/etc/nginx/sites_enabled/default.conf" ):
    ln(
        "/etc/nginx/sites_available/default.conf",
        "/etc/nginx/sites_enabled/default.conf" )
else:
    print( "el archivo de default existe" )


Chibi_path( '/var/www/default/' ).mkdir( is_ok_exists=True )
index = Chibi_file( "/var/www/default/index.html" )
index.write( "<h1>{} - waifus lab</h1>".format( get_hostname() ) )
command( 'chcon', '-Rt', 'httpd_sys_content_t', '/var/www/' )


systemctl.restart( "nginx" )


cowsay( "fin de inicio de nginx" )
