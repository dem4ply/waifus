#!/usr/bin/env python3
from chibi.config import basic_config
from chibi.file import Chibi_path
from chibi_command.echo import cowsay
from pprint import pprint


basic_config()

cowsay( "preparando filebeat" )

filebeat_config = Chibi_path( '/etc/filebeat/filebeat.yml' )
if not filebeat_config.exists:
    raise FileNotFoundError( f'no se encontro "{filebeat_config}" ' )
config = filebeat_config.open().read()

config[ 'output.elasticsearch' ].hosts = [ 'waifus' ]

pprint( config )
filebeat_config.open().write( config )

cowsay( "termino de preparar filebeat" )
