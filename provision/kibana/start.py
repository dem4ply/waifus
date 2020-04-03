#!/usr/bin/env python3
import os

from chibi.config import basic_config
from chibi.file import Chibi_path
from chibi_command.echo import cowsay
from chibi_command.nix import Systemctl


basic_config()
cowsay( "iniciando kibana" )

provision_folder = Chibi_path( os.environ[ 'PROVISION_PATH' ] )
provision_folder = provision_folder + 'elasticsearch' + 'provision'

kibana = provision_folder + "kibana.yml"
kibana.copy( '/etc/kibana/kibana.yml' )

Systemctl.restart( "kibana" ).run()

cowsay( "termino el inicio de kibana" )
