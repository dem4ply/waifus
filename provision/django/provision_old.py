#!/usr/bin/env python3
import os
import time

from chibi.atlas import Chibi_atlas
from chibi.config import basic_config
from chibi.file import Chibi_path
from chibi_command import lxc
from chibi_command.echo import cowsay
from chibi_command.nix import Systemctl
from chibi_command.rsync import Rsync
from chibi_command.centos import Iptables
from chibi_requests import Chibi_url


basic_config()
file_check_path = Chibi_path( '~/provision_installed' )
file_check = file_check_path.open()


provision_folder = Chibi_path( '/home/chibi/provision' )

port = 8000

basic_scripts = [
    provision_folder + 'install_python.sh',
    provision_folder + 'stuff/install_cowsay.py',
    (
        provision_folder + 'set_envars.py',
        '/home/chibi/provision/',
    ),
    provision_folder + 'copy_host.py',
    provision_folder + 'update_python_lib.sh',
    provision_folder + 'stuff/install_essential.py',
    provision_folder + 'stuff/install_ponysay.py',
    provision_folder + 'update_python_lib.sh',
    provision_folder + 'mariadb/install_client.py',
    ( provision_folder + 'add_user.py', 'chibi' )
]

celery_provision_script = (
    provision_folder + 'django' + 'celery_provision.py' )

django_projects = Chibi_atlas( {
    'quetzalcoatl_django': {
        'git_repo': 'https://github.com/dem4ply/quetzalcoatl.git',
        'scripts': basic_scripts,
        'systemd': [
            Chibi_path( 'quetzalcoatl/gunicorn.service' ),
        ],
    },
    'quetzalcoatl_celery': {
        'git_repo': 'https://github.com/dem4ply/quetzalcoatl.git',
        'scripts': basic_scripts + [
            ( provision_folder + 'add_user.py', 'celery' ),
            celery_provision_script
        ],
        'systemd': [
            Chibi_path( 'quetzalcoatl/celery.service' ),
        ],
    },

    'corona_chan_django': {
        'git_repo': 'https://github.com/dem4ply/quetzalcoatl.git',
        'scripts': basic_scripts,
        'systemd': [
            Chibi_path( 'corona_chan/gunicorn.service' ),
        ],
    },
    'corona_chan_celery': {
        'git_repo': 'https://github.com/dem4ply/corona_chan.git',
        'scripts': basic_scripts + [
            ( provision_folder + 'add_user.py', 'celery' ),
            celery_provision_script
        ],
        'systemd': [
            Chibi_path( 'corona_chan/celery.service' ),
        ],
    },
} )

provision_folder_host = Chibi_path( os.environ[ 'PROVISION_PATH' ] )
systemd_provision = provision_folder_host + 'django' + 'provision' + 'systemd'

containers = Chibi_path( '/var/lib/lxc/' )


def create_container( name ):
    version_to_check = f'{name} lxc'
    info = lxc.Info.name( name ).run()
    if not info:
        lxc.Create.name( name ).template( 'download' ).parameters(
            '--d', 'centos', '--r', '7', '--arch', 'amd64' ).run()


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


def add_user_chibi( name ):
    cowsay( f'clonando repo {name}' )
    script = prepare_script( provision_folder + 'add_user.py' )
    lxc.Attach.name( name ).run( *script, 'chibi' )


def copy_sysmted( name, props ):
    cowsay( 'copy systemd services' )
    root = containers + name + 'rootfs'
    systemd_root = root + 'etc' + 'systemd' + 'system'
    for s in props.systemd:
        systemd_service = systemd_provision + s
        envars = systemd_service.replace_extensions( 'env' )
        systemd_service.copy( systemd_root )
        if envars.exists:
            envars.copy( systemd_root )

    container = lxc.Attach.name( name )
    container.run( Systemctl.daemon_reload() )
    for s in props.systemd:
        s = s.file_name
        container.run( Systemctl.start( s ) )
        container.run( Systemctl.enable( s ) )
        time.sleep( 30 )
        container.run( Systemctl.status( s ) )


def install_dependencies( name, props ):
    cowsay( 'instalando dependencias' )
    chibi_home = Chibi_path( '/home' ) + 'chibi'

    git_repo_url = Chibi_url( props.git_repo )
    folder = git_repo_url.base_name.rsplit( '.git', 1 )[0]
    projects = chibi_home + 'projects'
    git_folder = projects + folder
    requirements = git_folder + 'requirements_dev.txt'
    lxc.Attach.name( name ).run( 'pip3', 'install', '-r', requirements )
    cowsay( 'termino de instalar dependencias' )


def prepare_script( script ):
    run = provision_folder + 'lxc' + 'run.sh'
    #return script,
    #return run, script
    if script.endswith( 'py' ):
        return 'python3', script
    return 'bash', script


for i, ( name, props ) in enumerate( django_projects.items() ):
    cowsay( f'iniciando contenedor {name}' )
    create_container( name )
    sync_provision( name )

    info = lxc.Info.name( name ).run()
    if not info.is_running:
        lxc.Start.name( name ).daemon().run()

    time.sleep( 10 )
    cowsay( f'ejecutando scripts en {name}' )
    container = lxc.Attach.name( name ).set_var(
        'PROVISION_PATH', provision_folder )
    for script in props.scripts:
        cowsay( f"ejecutando {script}" )
        if isinstance( script, tuple ):
            args = script[1:]
            script = script[0]
            container.run( *prepare_script( script ), *args )
        else:
            container.run( *prepare_script( script ) )

    add_user_chibi( name )
    clone_repo( name, props.git_repo )
    install_dependencies( name, props )
    copy_sysmted( name, props )
    info = lxc.Info.name( name ).run()

    port += i
    iptable = Iptables.table( 'nat' ).append( "PREROUTING" ).protocol( 'tcp' )
    iptable.in_interface( 'eth1' ).destination_port( 8000 ).jump( 'DNAT' )
    iptable.to_destination( info.result.ip, 8000 )
    iptable.run()

    "iptables -t nat -A PREROUTING -p tcp -i eth1 --dport 8001 -j DNAT --to-destination 10.0.3.235:8000"
