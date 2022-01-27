#!/usr/bin/env python3
import os
import sys
import time
import requests
from datetime import datetime
from pprint import pprint

from chibi.config import basic_config
from chibi.file import Chibi_file, Chibi_path
from chibi.parser import to_bool
from chibi_command.echo import cowsay
from chibi_command.nix import Systemctl
from chibi.file.other import Chibi_systemd


basic_config()
masters = [ 'Misuzu' ]
provision_folder = (
    Chibi_path( os.environ[ 'PROVISION_PATH' ] ) + 'elasticsearch/provision' )


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
        status = Systemctl.status( 'elasticsearch' ).run()
        status = status.result.properties.get( 'active_state', 'No' )
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
        'discovery.seed_hosts':  masters[:],
        'cluster.initial_master_nodes': masters[:],
        'path.data': '/var/data/waifus',
        'path.logs': '/var/log/waifus',
    }

    elastic_config = Chibi_file( '/etc/elasticsearch/elasticsearch.yml' )
    elastic_config.write( config, is_safe=True )
    pprint( elastic_config.read() )

    data = Chibi_path( '/var/data/waifus' )
    log = Chibi_path( '/var/log/waifus' )
    data.mkdir()
    log.mkdir()

    synonims = Chibi_path( '/etc/elasticsearch/synonyms' )

    if not synonims.exists:
        synonims.mkdir()

    synonyms_folder = provision_folder + 'synonyms'
    synonyms_folder.copy( synonims )

    synonims.chown( user_name='elasticsearch', group_name='elasticsearch' )
    data.chown( user_name='elasticsearch', group_name='elasticsearch' )
    log.chown( user_name='elasticsearch', group_name='elasticsearch' )

    service = Chibi_path( '/usr/lib/systemd/system/elasticsearch.service' )
    if not service.exists:
        print( "no se encontro {service}" )
    else:
        f = service.open( chibi_file_class=Chibi_systemd )
        result = f.read()
        try:
            del result.service.TimeoutSec
        except KeyError:
            pass
        result.service.TimeoutSec = '900'
        f.write( result )

    mem_options = Chibi_path( '/etc/elasticsearch/jvm.options.d/mem.options' )
    mem_options.open().write( "-Xms2g\n-Xmx2g\n" ) # 2GB

    Systemctl.restart( 'elasticsearch.service' ).run()
    #wait_until_elastic_is_up( name )

    cowsay( "termino de actualizar la configuracion de elasticsearch" )
