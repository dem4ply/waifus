rabbitmqctl delete_user madshopify
rabbitmqctl add_user madshopify password
rabbitmqctl add_vhost madshopify_vhost
rabbitmqctl set_user_tags madshopify madshopify_tag
rabbitmqctl set_permissions -p madshopify_vhost madshopify ".*" ".*" ".*"
