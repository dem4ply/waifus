#!/usr/bin/env python3
import logging
import os

from chibi_command import Command
from chibi.config import basic_config
from chibi.file import Chibi_path
from chibi.file.snippets import ln
from chibi.net.hostname import get_hostname
from chibi_command.echo import cowsay
from chibi_command.nix import Systemctl

basic_config()
logger = logging.getLogger( 'ssh.provision' )


provision_folder = (
    Chibi_path( os.environ[ 'PROVISION_PATH' ] )
    + 'ssh' + 'provision' )


cowsay( "inicia la provision de ssh" )

users = [ 'chibi' ]
ssh_folder = Chibi_path( '~/.ssh' )
ssh_config = provision_folder + 'config'
if ssh_config.exists:
    ssh_config += '*'
    if not ssh_folder.exists:
        ssh_folder.mkdir()
    ssh_config.copy( ssh_folder )
    keys = ssh_folder.find( r'.*\.pub', dirs=False, files=True )
    for key in keys:
        private_key = key.replace( '.pub', '' )
    publics = filter( lambda x: x.extension == 'pub', ssh_folder.ls() )
    for ssh_key in publics:
        private = ssh_key.replace( '.pub', '' )
        print( f"{private} chmod 0600" )
        private.chmod( 0o0600 )

    for user in users:
        ssh_folder = Chibi_path( f'/home/{user}/.ssh' )
        if not ssh_folder.exists:
            ssh_folder.mkdir()
        ssh_config.copy( ssh_folder )
        ssh_folder.chown(
            user_name='chibi', group_name='chibi', recursive=True )
        keys = ssh_folder.find( r'.*\.pub', dirs=False, files=True )
        for key in keys:
            private_key = key.replace( '.pub', '' )
        publics = filter( lambda x: x.extension == 'pub', ssh_folder.ls() )
        for ssh_key in publics:
            private = ssh_key.replace( '.pub', '' )
            print( f"{private} chmod 0600" )
            private.chmod( 0o0600 )


else:
    logger.warn( 'no se encontro el config ssh' )
