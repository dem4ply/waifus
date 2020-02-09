#!/usr/bin/env python3
import time
import sys
import yaml
import requests

from chibi.parser import to_bool
from chibi.command import command, systemctl
from chibi.file.snippets import exists, join, mkdir, chown, ls, copy
from chibi.command.echo import cowsay
from datetime import datetime
from chibi.file import Chibi_file, Chibi_path


masters = [ 'Pitou', 'Sakura', 'Misuzu' ]
FOLDER_PROVISION = Chibi_path( "/vagrant/provision/elasticsearch/provision" )


def is_time( start, max_wait_time ):
    current = ( datetime.utcnow() - start ).seconds
    if ( current > max_wait_time ):
        return True
    return False


def wait_until_elastic_is_up( name ):
    url = 'http://{}:9200'.format( name )
    start = datetime.utcnow()
    max_time_to_wait = 300

    while True:
        status = (
            systemctl.status( 'elasticsearch' )
                .properties.get( 'active_state', 'No' ) )
        try:
            response = requests.get( url )
        except requests.exceptions.RequestException:
            time.sleep( 10 )
            if is_time( start, max_time_to_wait ):
                print(
                    "termino en el tiempo de espera "
                    "cuando iniciava elastic" )
                break
            continue

        if ( status == 'active' and str( response.status_code ) == '200' ):
            break
        if is_time( start, max_time_to_wait ):
            print(
                "termino en el tiempo de espera "
                "revisando la respuesta de elastic" )
            break
        time.sleep( 5 )


if __name__ == "__main__":

    name = sys.argv[1]
    is_master = to_bool( sys.argv[2] )
    is_data = to_bool( sys.argv[3] )

    cowsay(
        "iniciando la configuracion de ES: {}, es maestro: {}, "
        "es nodo de datos: {}".format( name, is_master, is_data ) )

    config = {
        "cluster.name": 'waifus',
        'node.name': '${HOSTNAME}',
        'node.master': is_master,
        'node.data': is_data,
        'network.host': '${HOSTNAME}',
        'network.bind_host': '${HOSTNAME}',
        'discovery.seed_hosts':  masters[::],
        'cluster.initial_master_nodes': masters[::],
        'path.data': '/var/data/waifus',
        'path.logs': '/var/log/waifus',
    }

    elastic_config = Chibi_file( '/etc/elasticsearch/elasticsearch.yml' )
    elastic_config.write_yaml( config, is_safe=True )
    print( elastic_config.read() )

    mkdir( '/var/data/waifus', verbose=True )
    mkdir( '/var/log/waifus', verbose=True )

    if not exists( '/etc/elasticsearch/synonyms' ):
        mkdir( '/etc/elasticsearch/synonyms', verbose=True )

    synonyms_folder = FOLDER_PROVISION + 'synonyms'
    synonyms_folder.copy( '/etc/elasticsearch/synonyms/', verbose=True )

    chown(
        '/var/data/waifus', '/var/log/waifus', '/etc/elasticsearch/synonyms',
        user_name='elasticsearch', group_name='elasticsearch' )

    systemctl.restart( 'elasticsearch.service' )
    wait_until_elastic_is_up( name )

    cowsay( "termino de actualizar la configuracion de elasticsearch" )
