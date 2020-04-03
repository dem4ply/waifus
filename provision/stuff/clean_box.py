#!/usr/bin/env python3
from chibi.config import basic_config
from chibi.file import Chibi_path
from chibi_command.disk.dd import DD
from chibi_command.echo import cowsay


basic_config()
cowsay( "limpiando box" )

empty = Chibi_path( '/EMPTY' )

DD.to_zero( empty ).run()
empty.delete()

bash_history = Chibi_path( '/root/.bash_history' )
vagrant_history = Chibi_path( '/home/vagrant/.bash_history' )

if bash_history.exists:
    bash_history.delete()
if vagrant_history.exists:
    vagrant_history.delete()

cowsay( "termini de limpiar la box" )
