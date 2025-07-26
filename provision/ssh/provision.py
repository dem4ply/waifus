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

users = [ 'vagrant', 'chibi' ]
ssh_folder = Chibi_path( '~/.ssh' )
ssh_config = provision_folder + 'config'

if ssh_config.exists:
    # root ssh config
    ssh_config += '*'
    if not ssh_folder.exists:
        ssh_folder.mkdir()
    result = ssh_config.copy( ssh_folder )
    for r in result:
        r.chmod( 0x600 )

    for user in users:
        home = Chibi_path( f'/home/{user}' )
        if not home.exists:
            logger.info(
                f"no se encontro el '{home}' se salta la configuracion "
                f"de {user}" )
            continue
        ssh_folder = home + '.ssh'
        if not ssh_folder.exists:
            ssh_folder.mkdir()
        result = ssh_config.copy( ssh_folder )
        for r in result:
            r.chmod( 0x600 )
            r.chown( user_name=user, group_name=user )

else:
    logger.warn( 'no se encontro el config ssh' )
