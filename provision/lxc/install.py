#!/usr/bin/env python3
from chibi.file.snippets import inflate_dir
from chibi.file import Chibi_file
from chibi_command.centos import Yum
from chibi_command.nix import Systemctl
from chibi_command.echo import cowsay

file_check_path = inflate_dir( '~/provision_installed' )
file_check = Chibi_file( file_check_path )


django_projects = {
    'quetzalcoatl': 'git@github.com:dem4ply/quetzalcoatl.git'
}


version_to_check = "lxc\n".format( file=__file__, )


if __name__ == "__main__" and not version_to_check in file_check:
    cowsay( "Starting install for lxc" )
    Yum.install(
        'epel-release', 'debootstrap', 'perl', 'libvirt', 'lxc',
        'lxc-templates', 'lxc-extra'
    )
    Systemctl.start( 'lxc.service', 'libvirtd' )
    Systemctl.enable( 'lxc.service', 'libvirtd' )

    file_check.append( version_to_check )
    cowsay( "Ending install for lxc" )

    """
    lxc-checkconfig
    ls -alh /usr/share/lxc/templates/
    lxc-create -n container01 -t centos
    """
