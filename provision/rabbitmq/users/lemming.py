#!/usr/bin/env python3
from chibi.config import basic_config
from chibi.command import rabbitmq


basic_config()
rabbitmq.delete_user( 'lemming' )
rabbitmq.add_user( 'lemming', 'password' )
rabbitmq.delete_user( 'guest' )
rabbitmq.set_user_tags( 'lemming', 'administrator' )
rabbitmq.add_vhost( 'lemming_vhost' )
rabbitmq.set_permissions( 'lemming_vhost', 'lemming' )
