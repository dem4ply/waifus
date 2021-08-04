#!/usr/bin/env python3
from chibi.config import basic_config
from chibi.file import Chibi_path
from chibi.file.other import Chibi_conf
from chibi_command.echo import cowsay
from chibi_command.nix import Systemctl
from pprint import pprint


basic_config()


fpm_config_path = Chibi_path( '/etc/php-fpm.d/www.conf' )


if __name__ == "__main__":
    cowsay( "iniciando configuracion de php fpm" )
    conf = fpm_config_path.open( chibi_file_class=Chibi_conf )
    data = conf.read()
    pprint( data )

    data.www[ 'user' ] = 'chibi'
    data.www[ 'group' ] = 'chibi'
    data.www[ 'listen' ] = '127.0.0.1:9000'

    data.www[ 'chroot' ] = '/home/chibi/owncloud/'

    data.www[ 'env[HOSTNAME]' ] = '$HOSTNAME'
    data.www[ 'env[PATH]' ] = '/usr/local/bin:/usr/bin:/bin'
    data.www[ 'env[TMP]' ] = '/tmp'
    data.www[ 'env[TMPDIR]' ] = '/tmp'
    data.www[ 'env[TEMP]' ] = '/tmp'

    php_session = Chibi_path( '/var/lib/php/session' )
    if not php_session.exists:
        php_session.mkdir()

    php_session.chown( user_name='chibi', group_name='chibi', recursive=True )

    Systemctl.start( "php-fpm" ).run()
    Systemctl.enable( "php-fpm" ).run()

    cowsay( "terminando configuracion de php fpm" )
