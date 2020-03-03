#!/usr/bin/env python3
import os
import time

from chibi.config import basic_config
from chibi.file import Chibi_path
from chibi_command import lxc
from chibi_command.rsync import Rsync
from chibi.atlas import Chibi_atlas
from chibi_command.echo import cowsay
from chibi_command.nix import Systemctl


basic_config()
file_check_path = Chibi_path( '~/provision_installed' )
file_check = file_check_path.open()


provision_folder = Chibi_path( '/home/chibi/provision' )

django_projects = Chibi_atlas( {
    'quetzalcoatl': {
        'git_repo': 'https://github.com/dem4ply/quetzalcoatl.git',
        'scripts': [
            provision_folder + 'install_python.sh',
            provision_folder + 'stuff/install_cowsay.py',
            provision_folder + 'update_python_lib.sh',
            provision_folder + 'stuff/install_essential.py',
            provision_folder + 'stuff/install_ponysay.py',
            provision_folder + 'update_python_lib.sh',
        ],
        'systemd': [
            'quetzalcoalt_gunicorn.service',
        ],
    }
} )

provision_folder_host = Chibi_path( os.environ[ 'PROVISION_PATH' ] )
systemd_provision = provision_folder_host + 'django' + 'provision' + 'systemd'

containers = Chibi_path( '/var/lib/lxc/' )


def create_container( name ):
    version_to_check = f'{name} lxc'
    if version_to_check not in file_check:
        lxc.Create.name( name ).template( 'centos' ).run()
        file_check.append( version_to_check )


def sync_provision( name ):
    root = containers + name + 'rootfs'
    chibi_home = root + 'home' + 'chibi'
    chibi_provision = chibi_home
    chibi_provision.mkdir()
    Rsync.clone_dir().human().verbose().run(
        provision_folder_host, chibi_provision )


def clone_repo( name, url ):
    cowsay( f'clonando repo {name}' )
    script = prepare_script( provision_folder + 'django' + 'git_clone.py' )
    lxc.Attach.name( name ).run( *script, url )


def copy_sysmted( name, props ):
    cowsay( 'copy systemd services' )
    root = containers + name + 'rootfs'
    systemd_root = root + 'etc' + 'systemd' + 'system'
    for s in props.systemd:
        systemd_service = systemd_provision + s
        systemd_service.copy( systemd_root )
    Systemctl.daemon_reload()
    for s in props.systemd:
        Systemctl.start( s )
        Systemctl.enable( s )


def prepare_script( script ):
    if script.endswith( 'py' ):
        return 'python3', script
    return 'bash', script


for name, props in django_projects.items():
    cowsay( f'iniciando contenedor {name}' )
    create_container( name )
    sync_provision( name )

    info = lxc.Info.name( name ).run()
    if not info.is_running:
        lxc.Start.name( name ).daemon().run()

    cowsay( f'ejecutando scripts en {name}' )
    for script in props.scripts:
        cowsay( f"ejecutando {script}" )
        lxc.Attach.name( name ).run( *prepare_script( script ) )
        time.sleep( 1 )

    clone_repo( name, props.git_repo )
    copy_sysmted( name, props )
