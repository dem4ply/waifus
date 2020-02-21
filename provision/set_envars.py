#!/usr/bin/env python3
import sys
from chibi_command.echo import cowsay
from chibi.file import Chibi_path


provision_folder = Chibi_path( '/vagrant/provision' )
file_host = provision_folder + 'hosts'

dest = '/etc/hosts'

if __name__ == "__main__":
    path = sys.argv[1]
    provision = Chibi_path( '/etc/profile.d/provision.sh' )
    provision.open().write( f'export PROVISION_PATH={path}' )
