#!/usr/bin/env python3
import logging
import os

from chibi.config import basic_config
from chibi.file import Chibi_path
from chibi.net.hostname import get_hostname
from chibi_command.echo import cowsay
from python_hosts import Hosts, HostsEntry


basic_config()
logger = logging.getLogger( 'waifus.provision.copy_host' )
provision_folder = Chibi_path( os.environ[ 'PROVISION_PATH' ] )
file_host = provision_folder + 'hosts'

dest = Chibi_path( '/etc/hosts' )

if __name__ == "__main__":
    cowsay( "copy hosts file" )
    host = Hosts( file_host )

    logger.info( f"usando el archivo de {file_host}" )
    for line in dest.open().read().split( '\n' ):
        if line:
            logger.info( line )

    host_dest = Hosts( dest )
    host_dest.entries = []
    host_dest.add( [
        HostsEntry(
            entry_type='ipv4', address='127.0.0.1',
            names=[ 'localhost' ] ),
        HostsEntry(
            entry_type='ipv6', address='::1',
            names=[ 'localhost' ] ),
    ] )
    host_dest.add( host.entries )
    host_dest.write()

    logger.info( f"termino de escribir el {file_host}" )
    for line in dest.open().read().split( '\n' ):
        if line:
            logger.info( line )

    cowsay( "ending copy hosts file" )
