#!/usr/bin/env python3
import os
import logging
from chibi.config import basic_config
from chibi.file.snippets import ln
from chibi.file import Chibi_path
from chibi_command.centos import Yum
from chibi_command.echo import cowsay
from chibi_command.nix import Systemctl
from argparse import ArgumentParser

logger = logging.getLogger( 'nginx.enable' )


provision_folder = (
    Chibi_path( os.environ[ 'PROVISION_PATH' ] )
    + 'nginx' + 'provision' )


def copy_all_configs():
    folders = (
        "/var/log/nginx",
        "/etc/nginx/sites_available",
        "/etc/nginx/sites_enabled"
    )

    for folder in folders:
        Chibi_path( folder ).mkdir( verbose=True )

    folders = ( 'conf.d', "sites_available" )

    nginx_folder = Chibi_path( '/etc/nginx/' )

    for folder in folders:
        dest = nginx_folder + folder
        folders_for_copy = provision_folder + folder
        folders_for_copy.copy( dest )

    ( provision_folder + 'nginx.conf' ).copy( nginx_folder + 'nginx.conf' )

    sites_enabled = nginx_folder + 'sites_enabled'
    sites_available = nginx_folder + 'sites_available'
    return sites_enabled, sites_available


if __name__ == "__main__":
    basic_config()
    parser = ArgumentParser(
        description="habilita nginx confifuraciones", fromfile_prefix_chars='@'
    )

    parser.add_argument(
        "--user", '-u', dest="user", default="",
        help="usuario del sitio" )

    sub_parsers = parser.add_subparsers(
        dest='command', help='sub-command help' )

    parser_enable = sub_parsers.add_parser(
        'enable', help='enable configuracion', )
    parser_enable.add_argument(
        "config", nargs='+', metavar="config",
        help="configuracion que se quire habilitar" )

    parser_disable = sub_parsers.add_parser(
        'disable', help='disable configuracion', )
    parser_disable.add_argument(
        "config", nargs='+', metavar="config",
        help="configuracion que se quire desabilitar" )

    args = parser.parse_args()
    configs = args.config
    configs = list( ( f"{c}.conf" for c in configs ) )
    if args.command == 'enable':
        cowsay( f"activando configuracion {configs}" )
        enable, available = copy_all_configs()
        for config in configs:
            link = enable + config
            if not link.exists:
                ln( available + config, link )
            else:
                logger.info( f'el archivo {config} existe' )

    elif args.command == 'disable':
        cowsay( f"desabilitando configuracion {configs}" )
        enable, available = copy_all_configs()
        for config in configs:
            link = enable + config
            if link.exists:
                link.delete()
    else:
        raise NotImplementedError

    cowsay( "termino configuracion {config}" )
