#!/usr/bin/env python3
import sys
from chibi_command.echo import cowsay
from chibi.file import Chibi_path

dest = '/etc/hosts'

if __name__ == "__main__":
    path = sys.argv[1]
    profile = Chibi_path( '/etc/profile.d/' )
    provision = profile + 'provision.sh'
    provision.open().write( f'export PROVISION_PATH={path}' )
