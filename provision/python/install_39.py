#!/usr/bin/env python3
from chibi.config import basic_config
from chibi.file import Chibi_path
from chibi_command import Command
from chibi_command.echo import cowsay
from chibi_command.centos import Dnf


basic_config()
file_check_path = Chibi_path( '~/provision_installed' )
file_check = file_check_path.open()


version_to_check = "python39\n".format( file=__file__, )


if __name__ == "__main__" and not version_to_check in file_check:
    cowsay( "instalado python 3.9" )
    Dnf.install( 'python39' )
    cowsay( "termino de instalar python 3.9" )
    file_check.append( version_to_check )
