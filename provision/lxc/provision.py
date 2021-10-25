#!/usr/bin/env python3
import os
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
provision_ssh = (
    Chibi_path( os.environ[ 'PROVISION_PATH' ] ) + 'ssh/provision/' )


if __name__ == "__main__":
    if provision_ssh.exists:
        ssh_provision = Chibi_path(
            '/home/chibi/projects/waifus__master/provision/ssh/provision' )
        provision_ssh.copy( ssh_provision, verbose=True )
        for ssh_key in ssh_provision.ls():
            ssh_key.chmod( 0o0600 )
            ssh_key.chown( user_name='chibi', group_name='chibi', )

    first_machine = lxc.Create( '-n', 'test_machine' )
    first_machine.template( 'download' )
    first_machine.parameters(
        '-d', 'centos', '-r', '7', '--arch', 'amd64', '--keyserver',
        'hkp://keyserver.ubuntu.com' )
    first_machine.run()
    #first_machine = lxc.Destroy( '-n', 'asdf' )

    cd( '/home/chibi/projects/waifus__master' )
    Command( 'chibi_lxc', 'up', 'Ikaros', 'Asuka' ).run()
    Command( 'chibi_lxc', 'provision', 'Ikaros', 'Asuka' ).run()
    """
    ikaros = Command(
        'chibi_lxc', 'up', 'Ikaros', 'Misuzu', 'Pitou', 'Rei', 'Chii' )
    """
    #Chibi_path( 'hosts' ).copy( '/etc/hosts' )