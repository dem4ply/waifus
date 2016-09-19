#!/usr/bin/env python3
import yaml

cluster_name = 'waifus'
master = False
data = True
nodes = [ 'Sakura', 'Pitou', 'Misuzu', 'Ren', 'Sonico', 'Tifa', 'Rei', 'Rem' ]

path_data = '/var/data/waifus'
path_logs = '/var/log/waifus'

config = {
    "cluster.name": 'waifus',
    'node.master': False,
    'node.data': True,
    'discovery.zen.ping.multicast.enabled': False,
    'discovery.zen.ping.unicast.hosts': [ "Pitou", "Sakura", "Misuzu" ],
    'path.data': '/var/data/waifus',
    'path.logs': '/var/log/waifus',
}

config_node = {
    'Pitou': {
        'master': True,
        'data': True,
    },
    'Sakura': {
        'master': True,
        'data': True,
    },
    'Misuzu': {
        'master': True,
        'data': True,
    }
}

for node in nodes:
    if node in config_node:
        config[ 'node.data' ] = config_node[ node ][ 'data' ]
        config[ 'node.master' ] = config_node[ node ][ 'master' ]
    else:
        config[ 'node.data' ] = data
        config[ 'node.master' ] = master

    config[ 'network.host' ] = node
    config[ 'network.bind_host' ] = node
    config[ 'node.name' ] = node

    str_config = yaml.dump( config )
    with open ( 'provision/' + node + '.yml' , 'w' ) as file:
        file.write( str_config )


