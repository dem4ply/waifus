#!/usr/bin/env python3
from chibi.config import basic_config
from chibi_command.db import Mysql
from chibi_command.echo import cowsay


basic_config()
databases = [
    'reader_moe', 'test_reader_moe',
    'corona_chan', 'friends_on_demand', 'owncloud_db',
    'archivum', 'test_archivum',
]


if __name__ == "__main__":
    cowsay( "creando bases de datos" )
    mysql = Mysql.user( "root" ).password( 'password' )
    for db in databases:
        mysql.run_script(
            "CREATE DATABASE IF NOT EXISTS {};".format( db ) )


    mysql.run_script(
        "create user ownclouduser@localhost identified by 'ownclouduser@';" )
    mysql.run_script(
        "grant all privileges on owncloud_db.* to ownclouduser@localhost "
        "identified by 'ownclouduser@';" )
    mysql.run_script( "flush privileges;" )
