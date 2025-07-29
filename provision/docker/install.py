#!/usr/bin/env python3
import os
from chibi.config import basic_config
from chibi.file import Chibi_path
from chibi_command.centos import Dnf
from chibi_command.echo import cowsay
from chibi_command.nix import Systemctl
from chibi_command import Command
from chibi_command.sysctl import Sysctl
from chibi.file.snippets import ln


basic_config()
file_check_path = Chibi_path( '~/provision_installed' )
file_check = file_check_path.open()

provision_folder = (
    Chibi_path( os.environ[ 'PROVISION_PATH' ] ) + 'lxc/provision' )


version_to_check = "docker\n".format( file=__file__, )


if __name__ == "__main__" and not version_to_check in file_check:
    cowsay( "Starting install for docker" )
    Dnf.config_manager.add_repo(
        'https://download.docker.com/linux/centos/docker-ce.repo' )
    Dnf.install( 'docker', 'docker-compose-plugin' )

    file_check.append( version_to_check )
    cowsay( "Ending install for docker" )
