from chibi.command import yum, command, systemctl
from chibi.command.echo import cowsay
from chibi.file import inflate_dir, Chibi_file, copy, join, chown
from chibi.command import rpm


list_of_user_to_create = [ 'dem4ply', "root" ]
databases = [
    "dem4ply", "root", "turning_db_dev", "turning_db_test", "turn_profiling" ]


FOLDER_PROVISION="/home/vagrant/provision/postgresql/provision"

cowsay( "provisionado posrgresql" )

copy(
    join( FOLDER_PROVISION, "pg_hba.conf" ),
    "/var/lib/pgsql/data/pg_hba.conf", verbose=True )

chown(
    "/var/lib/pgsql/data/pg_hba.conf",
    user_name='postgres', group_name='postgres' )

copy(
    join( FOLDER_PROVISION, "postgresql.conf" ),
    "/var/lib/pgsql/data/postgresql.conf", verbose=True )

chown(
    "/var/lib/pgsql/data/postgresql.conf",
    user_name='postgres', group_name='postgres' )


for database in databases:
    command( "su", "postgres", "-c", "createdb {}".format( database ) )

for user in list_of_user_to_create:
    command( "su", "postgres", "-c", "createuser -d -s -r {}".format( user ) )
    command(
        "su", "postgres", "-c",
        "psql -c \"ALTER USER {} WITH PASSWORD 'asdf';\"".format( user ) )


systemctl.restart( "postgresql" )

cowsay( "termino de provisionado posrgresql" )
