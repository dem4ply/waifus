#!/usr/bin/env python3
from chibi.config import basic_config
from chibi_command.echo import cowsay
from chibi_command import Command


basic_config()
cowsay( "starting update vbox guest" )
Command( '/opt/VBoxGuestAdditions-5.*/init/vboxadd', 'setup' ).run()
cowsay( "ending update vbox guest" )
