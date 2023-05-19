#!/usr/bin/env python3
import sys
import logging
from chibi.config import basic_config
from chibi_command.db import Mysql
from chibi_command.echo import cowsay


basic_config()
logger = logging.getLogger( 'waifus.provision.mariadb.add_database' )


if __name__ == "__main__":
    cowsay( "creando bases de datos" )
    mysql = Mysql.user( "root" ).password( 'password' )
    database = sys.argv[1]
    logger.info( f"agregando base de datos {database}" )
    mysql.run_script(
        "CREATE DATABASE IF NOT EXISTS {};".format( database ) )
