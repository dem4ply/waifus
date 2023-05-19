#!/usr/bin/env python3
import os
import sys

from chibi.config import basic_config
from chibi.file import Chibi_path
from chibi_command.nix import Systemctl
from chibi_command.echo import cowsay


basic_config()
provision_folder = Chibi_path( os.environ[ 'PROVISION_PATH' ] )


origin = provision_folder + sys.argv[1]
target = Chibi_path( sys.argv[2] )

cowsay( f"iniciando copiando {origin} a {target}" )

origin.copy( target )

cowsay( f"terminando copiando {origin} a {target}" )
