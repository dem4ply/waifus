#!/usr/bin/env python3
import logging

from chibi.command.echo import cowsay
from chibi.file.snippets import Chibi_path
from chibi_command.centos import Yum, Firewall_cmd
from chibi_command.db import Mysql
from chibi_command.nix import Systemctl


logging.basicConfig( level=logging.INFO )


file_check_path = Chibi_path( '~/provision_installed' )
file_check = file_check_path.open()


version_to_check = "mariadb\n".format( file=__file__, )

remove_root = """
UPDATE mysql.user SET Password=PASSWORD('password') WHERE User='root';
DELETE FROM mysql.user WHERE User='root' AND Host NOT IN ('localhost', '127.0.0.1', '::1');
DELETE FROM mysql.user WHERE User='';
DELETE FROM mysql.db WHERE Db='test' OR Db='test_%';
CREATE USER 'dem4ply'@'%' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON *.* TO 'dem4ply'@'%';
FLUSH PRIVILEGES;
"""

if __name__ == "__main__" and not version_to_check in file_check:
    cowsay( "iniciando instalacion de mariadb" )
    Yum.install( "mariadb-server" )
    Systemctl.enable( "mariadb" )
    Systemctl.start( "mariadb" )

    mysql = Mysql.user( "root" )
    result = mysql.run_script( remove_root )
    print( vars( result ) )

    Firewall_cmd.add_port( '3306', kind='tcp', permanent=True )

    Systemctl.restart( "mariadb" )

    file_check.append( version_to_check )

    cowsay( "terminando la instalcion de mariadb" )
