#!/usr/bin/env python3
import logging

from chibi.command.echo import cowsay
from chibi_command.db import Mysql


logging.basicConfig( level=logging.INFO )

databases = [ 'notarius', 'reader_moe', 'test_reader_moe' ]

if __name__ == "__main__":
    cowsay( "creando bases de datos" )
    mysql = Mysql.user( "root" ).password( 'password' )
    for db in databases:
        mysql.run_script(
            "CREATE DATABASE IF NOT EXISTS {};".format( db ) )
