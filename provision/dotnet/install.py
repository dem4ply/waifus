#!/usr/bin/env python3
import os
from chibi.config import basic_config
from chibi.file import Chibi_path
from chibi_command.centos import Yum
from chibi_command.echo import cowsay
from chibi_command.nix import Systemctl
from chibi_command import Command
from chibi_command.sysctl import Sysctl
from chibi.file.snippets import ln


basic_config()
file_check_path = Chibi_path( '~/provision_installed' )
file_check = file_check_path.open()

provision_folder = (
    Chibi_path( os.environ[ 'PROVISION_PATH' ] ) + 'dotnet/provision' )


version_to_check = "dotnet\n".format( file=__file__, )


if __name__ == "__main__" and not version_to_check in file_check:
    cowsay( "instalando dotnet" )

    Yum.install(
        'dotnet-sdk-3.1','dotnet-runtime-3.1', 'aspnetcore-runtime-3.1'
    )

    file_check.append( version_to_check )
    cowsay( "termino de instalar dotnet" )
