from chibi.command import command
from chibi.command.echo import cowsay


cowsay( "starting update vbox guest" )
command( '/opt/VBoxGuestAdditions-5.1.10/init/vboxadd', 'setup' )
cowsay( "ending update vbox guest" )
