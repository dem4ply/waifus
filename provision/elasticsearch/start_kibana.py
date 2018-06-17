import sys
import yaml

from chibi.parser import to_bool
from chibi.command import command, systemctl
from chibi.file import exists, join, mkdir, chown, ls, copy
from chibi.command.echo import cowsay


cowsay( "iniciando kibana" )

FOLDER_PROVISION="/home/vagrant/provision/elasticsearch/provision"

copy(
    join( FOLDER_PROVISION, 'kibana.yml' ),
    '/etc/kibana/kibana.yml', verbose=True )

systemctl.restart( "kibana" )

cowsay( "termino el inicio de kibana" )
