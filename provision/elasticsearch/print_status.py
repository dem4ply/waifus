#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
import time
import requests
from datetime import datetime
from pprint import pprint

from chibi.config import basic_config
from chibi.file import Chibi_file, Chibi_path
from chibi.parser import to_bool
from chibi_command.echo import cowsay
from chibi_command.nix import Systemctl
from chibi.file.other import Chibi_systemd


basic_config()
provision_folder = (
    Chibi_path( os.environ[ 'PROVISION_PATH' ] ) + 'elasticsearch/provision' )



result = Systemctl.status( 'elasticsearch.service' ).run()
print( result.result.service )
for m in result.result.messages:
    print( '\t', m.get( 'MESSAGE', 'sin mensaje' ) )

#start = Systemctl.start( 'elasticsearch.service' )
#start.captive = False
#start.run()
