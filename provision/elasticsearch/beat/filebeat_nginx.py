#!/usr/bin/env python3
import itertools
from chibi.config import basic_config
from chibi.file import Chibi_path
from chibi_command.echo import cowsay
from pprint import pprint
from chibi.file.other.conf import Chibi_conf
from chibi_nginx import Chibi_nginx
from chibi.atlas import Chibi_atlas
import socket


basic_config()

cowsay( "preparando filebeat para nginx" )

filebeat_config = Chibi_path( '/etc/filebeat/filebeat.yml' )
if not filebeat_config.exists:
    raise FileNotFoundError( f'no se encontro "{filebeat_config}" ' )
config = filebeat_config.open().read()

config[ 'output.elasticsearch' ].enabled = False

config[ 'output.logstash' ] = {}
logstash = config[ 'output.logstash' ]
logstash.hosts = [ 'Tohru:5044' ]
logstash.enabled = True
logstash.worker = 1

config[ 'filebeat' ] = {}
filebeat = config[ 'filebeat' ]
inputs = config[ 'filebeat.inputs' ]
try:
    del filebeat.registry_file
except:
    pass
config[ 'filebeat.registry.file' ] = '/var/lib/filebeat/registry'

nginx_sites_enabled = Chibi_path( '/etc/nginx/sites_enabled/' )
hostname = socket.gethostname()


def is_nginx( d ):
    if 'fields' not in d:
        return False
    return 'nginx' in d.fields.tags

inputs = list( itertools.filterfalse( is_nginx, inputs ) )


for nginx_config in nginx_sites_enabled.ls():
    nginx_data = nginx_config.open( chibi_file_class=Chibi_nginx ).read()
    try:
        name = nginx_data.server.server_name
        access_log = nginx_data.server.access_log
        access_log = access_log.split( ' ', 1 )[0]
        error_log = nginx_data.server.error_log
    except ( KeyError, AttributeError ):
        continue
    if '$hostname' in name:
        name = name.replace( '$hostname', hostname )
    print( f'preparando "{name}" con "{access_log}" y "{error_log}"' )
    nginx_input = Chibi_atlas()
    nginx_input.type = 'log'
    nginx_input.exclude_files = [ ".gz$" ]

    nginx_input.fields = { 'tags': f'nginx, {name}, access' }
    nginx_input.fields.document_type = 'nginx-access'
    nginx_input.paths = [ f'{access_log}*' ]
    inputs.append( nginx_input.copy() )

    nginx_input.fields = { 'tags': f'nginx, {name}, error' }
    nginx_input.paths = [ f'{error_log}*' ]
    nginx_input.fields.document_type = 'nginx-error'
    inputs.append( nginx_input.copy() )

config[ 'filebeat.inputs' ] = inputs
pprint( config )
filebeat_config.open().write( config )

cowsay( "termino de preparar filebeat para nginx" )
