#!/usr/bin/env python3
import logging

from chibi.config import basic_config
from chibi_command.echo import cowsay
from chibi.file import Chibi_path
from chibi_command.centos import Yum, Firewall_cmd
from chibi_command.db import Mysql
from chibi_command.nix import Systemctl
from chibi_atlas import Chibi_atlas


basic_config()
file_check_path = Chibi_path( '~/provision_installed' )
file_check = file_check_path.open()


version_to_check = "mariadb\n".format( file=__file__, )

remove_root = """
SET PASSWORD FOR 'root'@'localhost' = PASSWORD('password');

DELETE FROM mysql.db WHERE Db='test' OR Db='test_%';
CREATE USER IF NOT EXISTS 'dem4ply'@'%' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON *.* TO 'dem4ply'@'%';
FLUSH PRIVILEGES;
"""


def do_query( mysql_captive, query ):
    result = mysql_captive.run_script( query )
    rows = result.result.split( '\n' )
    columns = rows[0].split( '\t' )
    result = []
    for row in rows[1:]:
        row = row.split( '\t' )
        result.append( Chibi_atlas( zip( columns, row ) ) )
    return result


def delete_empty_users( mysql, mysql_captive ):
    query = "SELECT User, Host FROM mysql.user where User=''"
    users = do_query( mysql_captive, query )
    for user in users:
        mysql.run_script( "DROP USER '{user.user}'@'{user.host}'" )

    query = (
        "DELETE FROM mysql.user "
        "WHERE User='root' AND Host NOT IN ('localhost', '127.0.0.1', '::1');"
    )
    users = do_query( mysql_captive, query )
    for user in users:
        mysql.run_script( "DROP USER '{user.user}'@'{user.host}'" )


if __name__ == "__main__" and not version_to_check in file_check:
    cowsay( "iniciando instalacion de mariadb" )
    Yum( 'module', 'enable', 'mariadb:10.11' ).run()
    Yum.install( "mariadb-server" )
    Systemctl.enable( "mariadb" ).run()
    Systemctl.start( "mariadb" ).run()

    mysql = Mysql.user( "root" )
    mysql_captive = Mysql.user( "root" )
    mysql_captive.captive = True
    result = mysql.run_script( remove_root )
    print( vars( result ) )
    delete_empty_users( mysql, mysql_captive )

    Firewall_cmd.add_port( '3306', kind='tcp', permanent=True )

    Systemctl.restart( "mariadb" ).run()

    file_check.append( version_to_check )

    cowsay( "terminando la instalcion de mariadb" )
