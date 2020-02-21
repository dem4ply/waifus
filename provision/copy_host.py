#!/usr/bin/env python3
from chibi_command.echo import cowsay
from chibi.file import Chibi_path


provision_folder = Chibi_path( '/vagrant/provision' )
file_host = provision_folder + 'hosts'

dest = '/etc/hosts'

if __name__ == "__main__":
    cowsay( "copy hosts file" )
    file_host.copy( dest )
    cowsay( "ending copy hosts file" )
