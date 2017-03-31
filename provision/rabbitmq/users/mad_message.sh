rabbitmqctl delete_user mad_message
rabbitmqctl add_user mad_message password
rabbitmqctl add_vhost mad_message_vhost
rabbitmqctl set_user_tags mad_message mad_message_tag
rabbitmqctl set_permissions -p mad_message_vhost mad_message ".*" ".*" ".*"
