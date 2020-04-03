#!/usr/bin/env python3
import os
from chibi.config import basic_config
from chibi.file import Chibi_path
from chibi_command.centos import Yum
from chibi_command.echo import cowsay
from chibi_command.nix import Systemctl
from chibi_command import Command
from chibi.file.snippets import ln


basic_config()
file_check_path = Chibi_path( '~/provision_installed' )
file_check = file_check_path.open()

provision_folder = (
    Chibi_path( os.environ[ 'PROVISION_PATH' ] ) + 'lxc/provision' )



django_projects = {
    'quetzalcoatl': 'git@github.com:dem4ply/quetzalcoatl.git'
}


version_to_check = "lxc\n".format( file=__file__, )


if __name__ == "__main__" and not version_to_check in file_check:
    cowsay( "Starting install for lxc" )
    #Yum.install( 'snapd' )
    #Systemctl.start( 'snapd.socket' ).run()
    #Systemctl.enable( 'snapd.socket' ).run()

    #grubby = Command( 'grubby' )
    #grubby.run(
    #    '--args="namespace.unpriv_enable=1"',
    #    '--update-kernel="$(grubby --default-kernel)"' )

    #grubby.run(
    #    '--args="usher_namespace.enable=1"',
    #    '--update-kernel="$(grubby --default-kernel)"' )

    #Chibi_path( '/etc/sysctl.d/99-userns.conf' ).open().write(
    #    'user.max_user_namespaces=3883' )

    #snap = Command( 'snap' )
    #snap.run( 'search', 'lxd' )
    #snap.run( 'install', 'lxd' )
    #ln( '/var/lib/snapd/snap', '/snap' )

    Yum.install(
        'epel-release', 'debootstrap', 'perl', 'libvirt', 'lxc',
        'lxc-templates', 'lxc-extra'
    )
    lxc_net_config = provision_folder + 'lxc-net'
    lxc_net_config.copy( '/etc/sysconfig/lxc-net' )

    Systemctl.start( 'lxc.service', 'libvirtd', 'lxc-net' ).run()
    Systemctl.enable( 'lxc.service', 'libvirtd', 'lxc-net' ).run()

    file_check.append( version_to_check )
    cowsay( "Ending install for lxc" )

    """
    lxc-checkconfig
    ls -alh /usr/share/lxc/templates/
    lxc-create -n container01 -t centos
    """
