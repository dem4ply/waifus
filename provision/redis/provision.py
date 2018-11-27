from chibi.command import yum, command, systemctl
from chibi.command.echo import cowsay
from chibi.file import inflate_dir, Chibi_file, copy, join, chown
from chibi.command import rpm


FOLDER_PROVISION="/home/vagrant/provision/redis/provision"

cowsay( "provisionado redis" )

copy( join( FOLDER_PROVISION, "redis.conf" ), "/etc/redis.conf", verbose=True )

systemctl.restart( "redis" )

cowsay( "termino de provisionado redis" )
