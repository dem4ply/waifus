#!/usr/bin/env python3
import sys
import yaml

from chibi.config import basic_config
from chibi.parser import to_bool
from chibi.command import command, systemctl
from chibi.file.snippets import exists, join, mkdir, chown, ls, copy
from chibi.command.echo import cowsay


basic_config()
cowsay( "iniciando kibana" )

FOLDER_PROVISION="/vagrant/provision/elasticsearch/provision"

copy(
    join( FOLDER_PROVISION, 'kibana.yml' ),
    '/etc/kibana/kibana.yml', verbose=True )

systemctl.restart( "kibana" )

cowsay( "termino el inicio de kibana" )
