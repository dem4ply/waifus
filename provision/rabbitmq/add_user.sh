rabbitmqctl add_user dem4ply pipiconpopo
rabbitmqctl delete_user guest
rabbitmqctl set_permissions -p / dem4ply ".*" ".*" ".*"
