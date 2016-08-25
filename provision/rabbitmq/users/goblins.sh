rabbitmqctl delete_user goblin
rabbitmqctl add_user goblin asdf
rabbitmqctl add_vhost goblin_vhost
rabbitmqctl set_user_tags goblin goblin_tag
rabbitmqctl set_permissions -p goblin_vhost goblin ".*" ".*" ".*"
