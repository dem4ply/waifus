#!/usr/bin/env python3
from chibi.config import basic_config
from chibi.command import command
from chibi.command.echo import cowsay


basic_config()
cowsay( "starting update vbox guest" )
command( '/opt/VBoxGuestAdditions-5.*/init/vboxadd', 'setup' )
cowsay( "ending update vbox guest" )
