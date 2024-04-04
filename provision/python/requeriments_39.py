#!/usr/bin/env python3
import os
import sys

from chibi.config import basic_config
from chibi.file import Chibi_path
from chibi_command import Command
from chibi_command.echo import cowsay


basic_config()
provision_folder = (
    Chibi_path( os.environ[ 'PROVISION_PATH' ] ) + 'django/provision' )

project_folder = Chibi_path( sys.argv[1] )
requeriments_txt = project_folder + sys.argv[2]

cowsay( f"provisionado {requeriments_txt}" )

pip = Command( 'pip3.9', 'install', '--upgrade', 'pip' )
pip.run()

pip = Command(
    'pip3.9', 'install', '-r', requeriments_txt )
pip.run()

cowsay( f"termino de provisionado {requeriments_txt}" )
