#!/usr/bin/env python3
import logging
import os

from chibi.config import basic_config
from chibi.command import command
from chibi.file import Chibi_path
from chibi.file.snippets import ln
from chibi.net.hostname import get_hostname
from chibi_command.echo import cowsay
from chibi_command.nix import Systemctl


basic_config()
logger = logging.getLogger( 'nginx.start' )


provision_folder = (
    Chibi_path( os.environ[ 'PROVISION_PATH' ] )
    + 'nginx' + 'provision' )


cowsay( "inicia de inicio de nginx" )

command( 'setsebool', '-P', 'httpd_can_network_connect', '1', )

folders = (
    "/var/log/nginx", "/etc/nginx/sites_available",
    "/etc/nginx/sites_enabled" )

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

configs = [ 'waifus.conf', 'kibana.conf', 'default.conf' ]

for config in configs:
    if not ( sites_enabled + config ).exists:
        ln( sites_available + config, sites_enabled + config )
    else:
        logger.info( 'el archivo {config} existe' )


Chibi_path( '/var/www/default/' ).mkdir( is_ok_exists=True )
index = Chibi_path( "/var/www/default/index.html" ).open()
index.write( "<h1>{} - waifus lab</h1>".format( get_hostname() ) )
command( 'chcon', '-Rt', 'httpd_sys_content_t', '/var/www/' )

Systemctl.restart( "nginx" )

cowsay( "fin de inicio de nginx" )
