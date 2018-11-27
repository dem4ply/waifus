from chibi.command import rabbitmq


rabbitmq.delete_user( 'turn_profile' )
rabbitmq.add_user( 'turn_profile', 'password' )
rabbitmq.delete_user( 'guest' )
rabbitmq.set_user_tags( 'turn_profile', 'administrator' )
rabbitmq.add_vhost( 'turn_profile_vhost' )
rabbitmq.set_permissions( 'turn_profile_vhost', 'turn_profile' )
