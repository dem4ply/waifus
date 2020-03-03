#!/usr/bin/env python3
import os
from chibi.config import basic_config
from chibi.file import Chibi_path
from chibi_command.echo import cowsay


basic_config()
provision_folder = Chibi_path( os.environ[ 'PROVISION_PATH' ] )
file_host = provision_folder + 'hosts'

dest = '/etc/hosts'

if __name__ == "__main__":
    cowsay( "copy hosts file" )
    file_host.copy( dest )
    cowsay( "ending copy hosts file" )
