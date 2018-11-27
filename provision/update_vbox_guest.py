#!/usr/bin/env python3
from chibi.command import command
from chibi.command.echo import cowsay


cowsay( "starting update vbox guest" )
command( '/opt/VBoxGuestAdditions-5.*/init/vboxadd', 'setup' )
cowsay( "ending update vbox guest" )
