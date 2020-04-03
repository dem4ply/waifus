rabbitmqctl delete_user dem4ply
rabbitmqctl add_user dem4ply 1234567890
rabbitmqctl delete_user guest
rabbitmqctl set_user_tags dem4ply administrator
rabbitmqctl set_permissions -p / dem4ply ".*" ".*" ".*"
