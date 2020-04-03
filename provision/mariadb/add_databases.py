#!/usr/bin/env python3
from chibi.config import basic_config
from chibi_command.db import Mysql
from chibi_command.echo import cowsay


basic_config()
databases = [
    'notarius', 'reader_moe', 'test_reader_moe', 'quetzalcoatl',
    'corona_chan' ]

if __name__ == "__main__":
    cowsay( "creando bases de datos" )
    mysql = Mysql.user( "root" ).password( 'password' )
    for db in databases:
        mysql.run_script(
            "CREATE DATABASE IF NOT EXISTS {};".format( db ) )
