#!/usr/bin/env python3
import os

from chibi.config import basic_config
from chibi.file import Chibi_path
from chibi_command import Command
from chibi_command.centos import Yum, Firewall_cmd
from chibi_command.echo import cowsay
from chibi_command.nix import Systemctl


basic_config()
provision_folder = (
    Chibi_path( os.environ[ 'PROVISION_PATH' ] ) + 'elasticsearch/provision' )


file_check_path = Chibi_path( '~/provision_installed' )
file_check = file_check_path.open()


version_to_check = "sql server\n".format( file=__file__, )


if __name__ == "__main__": #and not version_to_check in file_check:
    cowsay( "iniciando instalacion de sql server" )

    os.environ[ 'MSSQL_SA_PASSWORD' ] = "P@ssw0rd"
    os.environ[ 'ACCEPT_EULA' ] = "Y"

    Yum.install( "mssql-server", "mssql-tools", "unixODBC-devel" )
    mssql_conf = Command( '/opt/mssql/bin/mssql-conf' )
    sqlcmd = Command( '/opt/mssql-tools/bin/sqlcmd' )

    mssql = Chibi_path( '/var/opt/mssql/' )
    config_path = Chibi_path( '/var/opt/mssql/mssql.conf' )

    ( provision_folder + 'mssql.conf' ).copy( config_path )

    data = mssql + 'data'
    log = mssql + 'log'
    dump = mssql + 'dump'
    backup = mssql + 'backup'

    data.mkdir()
    log.mkdir()
    dump.mkdir()
    backup.mkdir()

    mssql.chown( user_name='mssql', group_name='mssql', recursive=True )
    mssql_conf( 'set', 'filelocation.defaultdatadir', str( data ) )
    mssql_conf( 'set', 'filelocation.defaultlogdir', str( log ) )
    mssql_conf( 'set', 'filelocation.defaultdumpdir', str( dump) )
    mssql_conf( 'set', 'filelocation.defaultbackupdir', str( dump) )
    mssql_conf( 'set', 'hadr.hadrenabled', '0' )
    mssql_conf( 'set', 'memory.memorylimitmb', '2000' )
    mssql_conf( 'set', 'network.tcpport', '1433' )

    mssql_conf( 'validate' )

    #print( config_path.open().read() )

    mssql_conf( '-n', 'set-sa-password' )



    Systemctl.enable( "mssql-server" ).run()
    Systemctl.start( "mssql-server" ).run()

    Firewall_cmd.add_port( '1433', kind='tcp', permanent=True )
    Firewall_cmd.reload()

    sqlcmd.captive = True
    result = sqlcmd(
        '-S', 'localhost,1433', '-U', 'SA', '-P', 'P@ssw0rd',
        '-Q', 'SELECT @@VERSION' )
    if result:
        cowsay( result.result )
    else:
        cowsay( str( vars( result ) ) )

    sql = (
        "CREATE LOGIN [dem4ply] WITH PASSWORD=N'P@ssw0rd', "
        "DEFAULT_DATABASE=[master], CHECK_EXPIRATION=ON, CHECK_POLICY=ON; "
        "ALTER SERVER ROLE [sysadmin] ADD MEMBER [dem4ply]" )

    result = sqlcmd(
        '-S', 'localhost,1433', '-U', 'SA', '-P', 'P@ssw0rd', '-Q', sql )
    if result:
        cowsay( result.result )
    else:
        cowsay( str( vars( result ) ) )


    file_check.append( version_to_check )

    cowsay( "terminando la instalcion de sql server" )
