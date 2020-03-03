#!/usr/bin/env python3
from chibi.config import basic_config
from chibi.command import rabbitmq


basic_config()
rabbitmq.delete_user( 'dem4ply' )
rabbitmq.add_user( 'dem4ply', '1234567890' )
rabbitmq.delete_user( 'guest' )
rabbitmq.set_user_tags( 'dem4ply', 'administrator' )
rabbitmq.set_permissions( '/', 'dem4ply' )
