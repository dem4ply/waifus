#!/usr/bin/env python3
from chibi.config import basic_config
from chibi_command.db import Mysql
from chibi_command.echo import cowsay

basic_config()

if __name__ == "__main__":
    cowsay( "agregando usuario de owncloud" )
    mysql = Mysql.user( "root" ).password( 'password' )
    mysql.run_script(
        "CREATE USER IF NOT EXISTS ownclouduser@localhost identified by 'ownclouduser@';" )
    mysql.run_script(
        "grant all privileges on owncloud_db.* to ownclouduser@localhost "
        "identified by 'ownclouduser@';" )
    mysql.run_script( "flush privileges;" )
    cowsay( "terminando de agregar usuario de owncloud" )
