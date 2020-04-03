#!/usr/bin/env python3
import sys
import logging

from chibi.config import basic_config
from chibi_command.echo import cowsay
from chibi_command.nix import User


basic_config()
logger = logging.getLogger( 'waifus.provision.add_user' )

user_name = sys.argv[1]

if __name__ == "__main__":
    cowsay( f"agregando el usuario {user_name}" )
    user = User.name( user_name )
    if user.exists:
        logger.info( f"el usuario {user_name} ya existe" )
    else:
        user.create()
    cowsay( f"terminando de agregar el usuario {user_name}" )
