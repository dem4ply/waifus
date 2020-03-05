#!/usr/bin/env python3
import os

from chibi.config import basic_config
from chibi.file import Chibi_path
from chibi.net.hostname import get_hostname
from chibi_command.echo import cowsay
from python_hosts import Hosts, HostsEntry


basic_config()
provision_folder = Chibi_path( os.environ[ 'PROVISION_PATH' ] )
file_host = provision_folder + 'hosts'

dest = '/etc/hosts'

if __name__ == "__main__":
    cowsay( "copy hosts file" )
    host = Hosts( file_host )
    host_dest = Hosts( dest )
    host_dest.add( [
        HostsEntry(
            entry_type='ipv4', address='1.0.0.127',
            names=[ 'localhost', get_hostname() ] ),
        HostsEntry(
            entry_type='ipv6', address='::1',
            names=[ 'localhost', get_hostname() ] ),
    ] )
    host_dest.add( host.entries )
    host_dest.write()
    cowsay( "ending copy hosts file" )
