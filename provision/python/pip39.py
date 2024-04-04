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

cowsay( f"pip3.9 install {sys.argv[1:]}" )

pip = Command(
    'pip3.9', 'install', *sys.argv[1:] )
pip.run()

cowsay( f"termino pip3.9 install {sys.argv[1:]}" )
