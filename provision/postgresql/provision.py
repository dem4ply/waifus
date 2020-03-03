#!/usr/bin/env python3
from chibi.config import basic_config
from chibi.command import command, systemctl
from chibi.command.echo import cowsay
from chibi.file.snippets import copy, join, chown


basic_config()
list_of_user_to_create = [ 'dem4ply', "root" ]
databases = [
    "dem4ply", "root", "turning_db_dev", "turning_db_test", "turn_profiling",
    "laniidae_db_dev", "lemming_db_dev" ]


FOLDER_PROVISION="/vagrant/provision/postgresql/provision"

cowsay( "provisionado posrgresql" )

copy(
    join( FOLDER_PROVISION, "pg_hba.conf" ),
    "/var/lib/pgsql/9.6/data/pg_hba.conf", verbose=True )

chown(
    "/var/lib/pgsql/9.6/data/pg_hba.conf",
    user_name='postgres', group_name='postgres' )

copy(
    join( FOLDER_PROVISION, "postgresql.conf" ),
    "/var/lib/pgsql/9.6/data/postgresql.conf", verbose=True )

chown(
    "/var/lib/pgsql/9.6/data/postgresql.conf",
    user_name='postgres', group_name='postgres' )


for database in databases:
    command( "su", "postgres", "-c", "createdb {}".format( database ) )
    command(
        "su", "postgres", "-c",
        "psql -d {} -c "
        "\"CREATE EXTENSION IF NOT EXISTS postgis;\"".format( database) )

for user in list_of_user_to_create:
    command( "su", "postgres", "-c", "createuser -d -s -r {}".format( user ) )
    command(
        "su", "postgres", "-c",
        "psql -c \"ALTER USER {} WITH PASSWORD 'asdf';\"".format( user ) )


systemctl.restart( "postgresql-9.6" )

cowsay( "termino de provisionado posrgresql" )
