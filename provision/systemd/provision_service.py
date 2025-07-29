#!/usr/bin/env python3
import os
import sys

from chibi.config import basic_config
from chibi.file import Chibi_path
from chibi_command.nix import Systemctl
from chibi_command.echo import cowsay
from chibi_atlas import Chibi_atlas, Chibi_atlas_default
from chibi.file.other import Chibi_systemd
from jinja2 import Template
from argparse import ArgumentParser


basic_config()
provision_folder = Chibi_path( os.environ[ 'PROVISION_PATH' ] )

parser = ArgumentParser(
    description="provisina un service para systemd", fromfile_prefix_chars='@'
)

parser.add_argument(
    "--name", '-n', dest="name", required=True,
    help="nombre del service" )

parser.add_argument(
    "--project_name", dest="project_name", required=True,
    help="nombre del projecto para los envars" )

parser.add_argument(
    "--environment", '-e', dest="environment", required=False,
    help="nombre del enviroment a copiar" )

service_common = Chibi_atlas_default()

service_common.unit.Description = 'servicio comun por default'

service_common.service.Type = 'simple'
service_common.service.User = 'chibi'
service_common.service.Group = 'chibi'


#service_common.service.WorkingDirectory = '/home/chibi/projects/'
#service_common.service.EnvironmentFile = '/etc/systemd/system/celery.env'
#service_common.service.ExecStart = "/bin/sh -c '/usr/local/bin/celery -A"

service_common.install.WantedBy = 'multi-user.target'


if __name__ == "__main__":
    basic_config()

    args = parser.parse_args()
    cowsay( f"creando systemd service {args.name}" )
    environment = args.environment

    systemd_root = Chibi_path( '/etc/systemd/system' )
    systemd_path = systemd_root + f'{args.name}.service'

    systemd_file = systemd_path.open( chibi_file_class=Chibi_systemd )
    del service_common.unit.Description
    service_common.unit.Description = f'servicio comun para {args.name}'

    systemd_file.write( service_common )

    if environment:
        environment_path = provision_folder + 'systemd' + 'environment'
        environment_path = environment_path + f"{environment}.env"
        if not environment_path.exists:
            raise NotImplementedError(
                "no existe el enviroment '{environment}'" )
        template = Template( environment_path.open().read() )
        result = template.render( project_slug=args.project_name )

        environment_result = systemd_root + f'{args.name}.env'
        environment_result.open().write( result )
    cowsay( f"termino de crear systemd service {args.name}" )
