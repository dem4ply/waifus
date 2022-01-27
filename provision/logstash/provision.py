#!/usr/bin/env python3
import os
from chibi.config import basic_config
from chibi.file import Chibi_path
from chibi_command.centos import Yum
from chibi_command.echo import cowsay


basic_config()

provision_folder = (
    Chibi_path( os.environ[ 'PROVISION_PATH' ] )
    + 'logstash' + 'provision' )

conf = provision_folder + 'conf'
patterns = provision_folder + 'patterns'



if __name__ == "__main__":
    cowsay( "Starting provision for logstash" )

    conf.copy( '/etc/logstash/conf.d/' )
    patterns.copy( '/etc/logstash/patterns/' )

    cowsay( "Ending provision for logstash" )
