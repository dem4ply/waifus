rabbitmqctl delete_user mad_hookshot
rabbitmqctl add_user mad_hookshot password
rabbitmqctl add_vhost mad_hookshot_vhost
rabbitmqctl set_user_tags mad_hookshot mad_hookshot_tag
rabbitmqctl set_permissions -p mad_hookshot_vhost mad_hookshot ".*" ".*" ".*"
