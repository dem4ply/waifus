#!/usr/bin/env python3
from chibi.config import basic_config
from chibi.file import Chibi_path
from chibi_command.centos import Yum
from chibi_command.echo import cowsay
from chibi_command.nix import Localectl


basic_config( level='DEBUG' )


if __name__ == "__main__":
    cowsay( "configuracion basica de centos" )
    Localectl.set_locale( 'es_MX.utf8' ).run()
    cowsay( "termino configuracion basica de centos" )
