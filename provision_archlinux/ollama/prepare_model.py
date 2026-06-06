#!/usr/bin/env python3
import sys
import logging
from chibi.config import basic_config
from chibi.file import Chibi_path
from chibi_command import Command, Result_error
from chibi_command.echo import cowsay
from chibi_command.archilinux import Pacman
from chibi_command.nix import Systemctl
from chibi_argsparser.common import Chibi_args
from chibi.file.other import Chibi_systemd


parser = Chibi_args()
parser.name.help = "nombre del modelo"
parser.name.required = True

parser.command.set_as_subparser()
parser.command.pull.help = "descarga un modelo"

logger = logging.getLogger( "ollama.prepare_model" )


def install_package( name ):
    Pacman.sync().no_confirm().run( name )


def main():
    ollama = Command( 'ollama' )

    args = parser()
    if args.command.pull:
        ollama.run( "pull", args.name )
    else:
        print( args )

if __name__ == "__main__":
    sys.exit( main() )  # pragma: no cover
