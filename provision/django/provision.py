#!/usr/bin/env python3
from chibi.file.snippets import inflate_dir
from chibi.file import Chibi_file, Chibi_path
from chibi_command import lxc
from chibi_command.rsync import Rsync
from chibi.atlas import Chibi_atlas
import time

file_check_path = inflate_dir( '~/provision_installed' )
file_check = Chibi_file( file_check_path )

"""
Script.new( "provision/install_python.sh" ),
Python.new( "provision/stuff/install_cowsay.py" ),
Script.new( "provision/update_python_lib.sh" ),
Python.new( "provision/update_centos.py" ),
Python.new( "provision/copy_host.py" ),
Python.new( "provision/stuff/install_essential.py" ),
Python.new( "provision/stuff/install_ponysay.py" ),
Python.new( "provision/repos/cp_all_repos.py" ),
Python.new( "provision/stuff/clean_box.py" ),

			Python.new( "provision/stuff/install_cowsay.py" ),
"""


provision_folder = Chibi_path( '/home/chibi/provision/provision' )

django_projects = Chibi_atlas( {
    'quetzalcoatl': {
        'git_repo': 'git@github.com:dem4ply/quetzalcoatl.git',
        'scripts': [
            provision_folder + 'install_python.sh',
            provision_folder + 'stuff/install_cowsay.py',
            provision_folder + 'update_python_lib.sh',
            provision_folder + 'stuff/install_essential.sh',
            provision_folder + 'stuff/install_ponysay.py',
        ]
    }
} )


provision_host = Chibi_path( '/vagrant/' )
containers = Chibi_path( '/var/lib/lxc/' )


def create_container( name ):
    version_to_check = f'{name} lxc'
    if version_to_check not in file_check:
        lxc.Create.name( name ).template( 'centos' ).run()
        file_check.append( version_to_check )


def sync_provision( name ):
    root = containers + name + 'rootfs'
    chibi_home = root + 'home' + 'chibi'
    chibi_provision = chibi_home + 'provision'
    chibi_provision.mkdir()
    Rsync.clone_dir().human().verbose().run( provision_host, chibi_provision )


def prepare_script( script ):
    if script.endswith( 'py' ):
        return 'python3', script
    return 'bash', script


for name, props in django_projects.items():
    create_container( name )
    sync_provision( name )

    lxc.Start.name( name ).daemon().run()
    for script in props.scripts:
        lxc.Attach.name( name ).run( *prepare_script( script ) )
        time.sleep( 1 )
