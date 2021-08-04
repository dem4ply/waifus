#!/usr/bin/env python3
import zipfile
from chibi.config import basic_config
from chibi.file import Chibi_path
from chibi_command.centos import Yum
from chibi_command.echo import cowsay
from chibi.file.temp import Chibi_temp_path


basic_config()
file_check_path = Chibi_path( '~/provision_installed' )
file_check = file_check_path.open()


version_to_check = "owncloud\n".format( file=__file__, )

owncloud_url = Chibi_url(
    'https://download.owncloud.org/community/owncloud-9.1.2.zip' )


owncloud_final = Chibi_path( '/home/chibi/owncloud/' )


if __name__ == "__main__" and not version_to_check in file_check:
    cowsay( "iniciando instalacion de owncloud" )
    download_path = Chibi_temp_path()
    owncloud_path = owncloud_url.download( download_path )
    with zipfile.ZipFile( owncloud_path, 'r' ) as z:
        z.extractall( owncloud_final )

    owncloud_final.chown(
        user_name='chibi', group_name='chibi', recursive=True )

    file_check.append( version_to_check )
    cowsay( "terminando instalacion de owncloud" )
