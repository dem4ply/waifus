#!/usr/bin/env python3
import os
from chibi.config import basic_config
from chibi.file import Chibi_path
from chibi_command.centos import Yum
from chibi_command.echo import cowsay
from chibi.net.hostname import get_hostname
from chibi_command.nix import Systemctl
from chibi_command import Command


provision_folder = (
    Chibi_path( os.environ[ 'PROVISION_PATH' ] )
    + 'nginx' + 'provision' )


basic_config()


if __name__ == "__main__":
    cowsay( "provisinando basico de nginx" )

    folders = (
        "/var/log/nginx",
        "/etc/nginx/sites_available",
        "/etc/nginx/sites_enabled"
    )
    for folder in folders:
        Chibi_path( folder ).mkdir( verbose=True )

    folders = ( 'conf.d', "sites_available" )

    nginx_folder = Chibi_path( '/etc/nginx/' )

    for folder in folders:
        dest = nginx_folder + folder
        folders_for_copy = provision_folder + folder
        folders_for_copy.copy( dest )

    ( provision_folder + 'nginx.conf' ).copy( nginx_folder + 'nginx.conf' )

    sites_enabled = nginx_folder + 'sites_enabled'
    sites_available = nginx_folder + 'sites_available'

    Chibi_path( '/var/www/default/' ).mkdir( is_ok_exists=True )
    index = Chibi_path( "/var/www/default/index.html" ).open()
    index.write( "<h1>{} - waifus lab</h1>".format( get_hostname() ) )
    Command( 'chcon', '-Rt', 'httpd_sys_content_t', '/var/www/' ).run()

    cowsay( "termino provisinando basico de nginx" )
