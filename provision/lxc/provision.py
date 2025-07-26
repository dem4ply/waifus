#!/usr/bin/env python3
import os
import logging
from chibi.config import basic_config
from chibi.file import Chibi_path
from chibi_command.centos import Yum
from chibi_command.echo import cowsay
from chibi_command.nix import Systemctl
from chibi_command import Command
from chibi_command.sysctl import Sysctl
from chibi_command import lxc
from chibi.file.snippets import ln
from chibi.file.snippets import cd


basic_config()
file_check_path = Chibi_path( '~/provision_installed' )
file_check = file_check_path.open()

provision_folder = (
    Chibi_path( os.environ[ 'PROVISION_PATH' ] ) + 'lxc/provision' )


vm_max_map_str = """
vm.max_map_count = 2147483642
fs.file-max = 2097152
"""

sysctl_conf = Chibi_path( "/etc/sysctl.d/99-max-map-count.conf" )


if __name__ == "__main__":
    sysctl_conf.open().write( vm_max_map_str )

    try:
        first_machine = lxc.Destroy( '-n', 'asdf' )
    except:
        logger.exception( f"fallo la destrucion de la maquina inicial asdf" )

    first_machine = lxc.Create( '-n', 'asdf' )
    first_machine.template( 'download' )
    first_machine.parameters(
        '-d', 'rocky', '-r', '9', '--arch', 'amd64',
        #'--keyserver', 'hkp://keyserver.ubuntu.com',
    )
    first_machine.run()
    first_machine = lxc.Destroy( '-n', 'asdf' )

    cd( '/home/chibi/projects/waifus' )
    ikaros = Command(
        'chibi_lxc', 'up', 'Ikaros', 'Misuzu', 'Pitou', 'Rei', 'Chii' )
    ikaros.run()
    #Chibi_path( 'hosts' ).copy( '/etc/hosts' )
