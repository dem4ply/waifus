#!/usr/bin/env python3
from chibi.config import basic_config
from chibi.file.snippets import cd
from chibi.net import download
from chibi_command import Command
from chibi_command.centos import Yum
from chibi_command.echo import cowsay


basic_config()
cowsay( "instalasion daskboards de kibana" )
cd( '/tmp/' )
download(
    'https://download.elastic.co/beats/dashboards/beats-dashboards-1.1.0.zip',
    file_name='beats-dashboards.zip' )

Yum.install( 'unzip' ).run()
Command( 'unzip', 'beats-dashboards.zip' ).run()
cd ( 'beats-dashboards' )
Command( './load.sh', '-l', 'waifus:80' ).run()

cowsay( "fin de instalasion de los dashboards de kibana" )
