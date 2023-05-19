#!/usr/bin/env python3
import zipfile
from chibi.config import basic_config
from chibi.file import Chibi_path
from chibi_command.centos import Yum
from chibi_command.echo import cowsay
from chibi.file.temp import Chibi_temp_path
from chibi_requests import Chibi_url
from chibi_command.file import Tar


basic_config()
file_check_path = Chibi_path( '~/provision_installed' )
file_check = file_check_path.open()


version_to_check = "owncloud\n".format( file=__file__, )

owncloud_url = Chibi_url(
    'https://download.owncloud.com/server/stable/'
    'owncloud-complete-latest.tar.bz2' )


tar_extraction_dir = Chibi_path( '/var/www/' )
owncloud_final = Chibi_path( '/var/www/owncloud' )


if __name__ == "__main__" and not version_to_check in file_check:
    cowsay( "iniciando instalacion de owncloud" )
    download_path = Chibi_temp_path()
    owncloud_path = owncloud_url.download( download_path )
    tar = Tar.verbose().extract().file( owncloud_path )
    tar = tar.output_directory( tar_extraction_dir )
    tar.run()

    owncloud_final.chown(
        user_name='apache', recursive=True )

    file_check.append( version_to_check )
    cowsay( "terminando instalacion de owncloud" )
