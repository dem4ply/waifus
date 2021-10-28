#!/usr/bin/env python3
from chibi.config import basic_config
from chibi_command.db import Mysql
from chibi_command.echo import cowsay


basic_config()
databases = [
    'sigrha__users',
    'sigrha__users__test',
    'sigrha_client',
    'sigrha_client__test',
    'sigrha_opportunities',
    'sigrha_opportunities__test',
    'sigrha_employees',
    'sigrha_employees__test',
]


if __name__ == "__main__":
    cowsay( "creando bases de datos" )
    mysql = Mysql.user( "root" ).password( 'password' )
    for db in databases:
        mysql.run_script(
            "CREATE DATABASE IF NOT EXISTS {};".format( db ) )

    mysql.run_script( "flush privileges;" )
