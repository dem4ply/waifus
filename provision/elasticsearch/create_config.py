import sys
import yaml

from chibi.parser import to_bool
from chibi.command import command, systemctl
from chibi.file import exists, join, mkdir, chown, ls, copy
from chibi.command.echo import cowsay


masters = [ 'Pitou', 'Sakura', 'Mizusu' ]
FOLDER_PROVISION="/home/vagrant/provision/elasticsearch/provision"

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
        'discovery.zen.ping.unicast.hosts': masters,
        'path.data': '/var/data/waifus',
        'path.logs': '/var/log/waifus',
    }

    str_config = yaml.dump( config )

    with open ( '/etc/elasticsearch/elasticsearch.yml', 'w' ) as file:
        file.write( str_config )

    mkdir( '/var/data/waifus', verbose=True )
    mkdir( '/var/log/waifus', verbose=True )

    if not exists( '/etc/elasticsearch/synonyms' ):
        mkdir( '/etc/elasticsearch/synonyms', verbose=True )

    synonyms_folder = join( FOLDER_PROVISION, 'synonyms' )
    synonyms = filter( lambda f: f.endswith( '.txt' ), ls( synonyms_folder ) )
    for source in synonyms:
        copy(
            join( synonyms_folder, source ), '/etc/elasticsearch/synonyms/',
            verbose=True )

    chown(
        '/var/data/waifus', '/var/log/waifus', '/etc/elasticsearch/synonyms',
        user_name='elasticsearch', group_name='elasticsearch' )

    systemctl.restart( 'elasticsearch.service' )

    cowsay( "termino de actualizar la configuracion de elasticsearch" )
