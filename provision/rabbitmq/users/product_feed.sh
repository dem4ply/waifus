rabbitmqctl delete_user product_feed
rabbitmqctl add_user madshopify password
rabbitmqctl add_vhost product_feed_vhost
rabbitmqctl set_user_tags product_feed product_feed_tag
rabbitmqctl set_permissions -p product_feed_vhost product_feed ".*" ".*" ".*"
