rabbitmqctl delete_user pf_api
rabbitmqctl add_user pf_api password
rabbitmqctl add_vhost pf_api_vhost
rabbitmqctl set_user_tags pf_api pf_api_tag
rabbitmqctl set_permissions -p pf_api_vhost pf_api ".*" ".*" ".*"
