#!/usr/bin/env python3
import sys
from chibi.config import basic_config
from chibi.file import Chibi_path
from chibi_command import Command, Result_error
from chibi_command.echo import cowsay
from chibi_command.archilinux import Pacman
from chibi_argsparser.common import Chibi_args


parser = Chibi_args()
parser.name.help = "nombre del paquete que se quiere instalar"
parser.name.required = True

parser.command.set_as_subparser()
parser.command.install.help = "instala o actualiza el paquete"


def install_package( name ):
    Pacman.sync().no_confirm().run( name )


def main():
    args = parser()

    name = args.name
    package = Pacman.query().info( name )
    try:
        result = package.run()
    except Result_error:
        if args.command.install:
            install_package( name )
        else:
            raise

    if args.command.install:
        install_package( name )
        result = package.run()
    result = result.result
    cowsay( (
        f'Paquete: "{result.name}" esta instalado con la '
        f'version: "{result.version}"'
    ) )

if __name__ == "__main__":
    sys.exit( main() )  # pragma: no cover
