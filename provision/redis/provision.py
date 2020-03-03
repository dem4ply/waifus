#!/usr/bin/env python3
from chibi.config import basic_config
from chibi.command import yum, command, systemctl
from chibi.command.echo import cowsay
from chibi.file.snippets import inflate_dir, copy, join, chown
from chibi.file import Chibi_file
from chibi.command import rpm


basic_config()
FOLDER_PROVISION="/vagrant/provision/redis/provision"

cowsay( "provisionado redis" )

copy( join( FOLDER_PROVISION, "redis.conf" ), "/etc/redis.conf", verbose=True )

systemctl.restart( "redis" )

cowsay( "termino de provisionado redis" )
