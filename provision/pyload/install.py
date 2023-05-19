#!/usr/bin/env python3
from chibi.config import basic_config
from chibi.file import Chibi_file, Chibi_path
from chibi_command import Command
from chibi_command.echo import cowsay


basic_config()
file_check_path = Chibi_path( '~/provision_installed' )
file_check = Chibi_file( file_check_path )


if __name__ == "__main__":
    cowsay( "instalando pyload" )
    Command( 'pip3', 'install', 'pyload-ng[all]' ).run()
    cowsay( "termino de instalar pyload" )
