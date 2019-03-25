#!/usr/bin/env python3
from chibi.command.disk.dd import dd_zero_to
from chibi.file.snippets import delete, exists
from chibi.command.echo import cowsay

cowsay( "limpiando box" )

dd_zero_to( '/EMPTY' )

delete( '/EMPTY' )
if exists( '/root/.bash_history' ):
    delete( '/root/.bash_history' )

if exists( '/home/vagrant/.bash_history' ):
    delete( '/home/vagrant/.bash_history' )

cowsay( "termini de limpiar la box" )
