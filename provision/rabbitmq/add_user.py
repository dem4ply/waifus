#!/usr/bin/env python3
from chibi.config import basic_config
from chibi_command.rabbitmq import Rabbitmqctl


users = [ 'corona_chan', 'quetzalcoatl', 'goblin' ]


basic_config()
Rabbitmqctl.delete_user( 'dem4ply' )
Rabbitmqctl.add_user( 'dem4ply', '1234567890' )
Rabbitmqctl.delete_user( 'guest' )
Rabbitmqctl.set_user_tags( 'dem4ply', 'administrator' )
Rabbitmqctl.set_permissions( '/', 'dem4ply' )

for user in users:
    Rabbitmqctl.delete_user( user )
    Rabbitmqctl.add_user( user, 'password' )
    Rabbitmqctl.set_user_tags( user, 'administrator' )
    Rabbitmqctl.add_vhost( f'{user}_vhost' )
    Rabbitmqctl.set_permissions( f'{user}_vhost', user )
