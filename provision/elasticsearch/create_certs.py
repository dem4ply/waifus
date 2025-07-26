#!/usr/bin/env python3
import os
import sys
import time
import requests
import shutil
from datetime import datetime
from pprint import pprint

from chibi.config import basic_config
from chibi.file import Chibi_file, Chibi_path
from chibi.parser import to_bool
from chibi_command.echo import cowsay
from chibi_command.nix import Systemctl
from chibi_command import Command
from chibi.file.other import Chibi_systemd
from chibi.file.temp import Chibi_temp_path


basic_config()
machines = [
    'Misuzu',
    'Rei',
    'Tohru',
    'Pochi',
]

certs_path = Chibi_path( 'home/chibi/elasticsearch/certs' )

elastic_certutil = Command(
    '/usr/share/elasticsearch/bin/elasticsearch-certutil' )

if __name__ == "__main__":
    # si los certificados existen y estan en su lugar no hace nada
    if certs_path.exists:
        for m in machines:
            c = certs_path + m
            if not c.exists:
                break
        else:
            ca_path = certs_path + 'ca'
            if ca_path.exists:
                sys.exit( 0 )

    cowsay(
        f"iniciando la creacion de certificados" )


    #temp = Chibi_temp_path()
    temp = Chibi_path( '/tmp/test_test' )
    if temp.exists:
        temp.delete()
    temp.mkdir()
    instance_path = temp + 'instance.yml'
    instance = []
    for m in machines:
        instance.append( { 'name': m, 'dns': m } )
    instance_path.open().write( { 'instances': instance } )
    cert_path = temp + 'certs.zip'

    elastic_certutil.run(
        'cert', '--keep-ca-key', '--pem',
        '--in', instance_path,
        '--out', cert_path,
    )

    unpack_certs = temp + 'certs'
    unpack_certs.mkdir()

    shutil.unpack_archive(
        str( cert_path ), extract_dir=str( unpack_certs ) )

    unpack_certs.move( certs_path )

    cowsay(
        f"termino la creacion de certificados" )
