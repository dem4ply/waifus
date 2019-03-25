#!/usr/bin/env python3
from chibi.command import rabbitmq


rabbitmq.delete_user( 'laniidae' )
rabbitmq.add_user( 'laniidae', 'password' )
rabbitmq.delete_user( 'guest' )
rabbitmq.set_user_tags( 'laniidae', 'administrator' )
rabbitmq.add_vhost( 'laniidae_vhost' )
rabbitmq.set_permissions( 'laniidae_vhost', 'laniidae' )
