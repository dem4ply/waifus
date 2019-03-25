rabbitmqctl delete_user laniidae
rabbitmqctl add_user laniidae asdf
rabbitmqctl add_vhost laniidae_vhost
rabbitmqctl set_user_tags laniidae laniidae_tag
rabbitmqctl set_permissions -p laniidae_vhost laniidae ".*" ".*" ".*"
