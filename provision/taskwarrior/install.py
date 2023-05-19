#!/usr/bin/env python3
from chibi.config import basic_config
from chibi.file import Chibi_path
from chibi.file.temp import Chibi_temp_path
from chibi_command.centos import Dnf
import zipfile
from chibi.config import basic_config
from chibi.file import Chibi_path
from chibi_command.centos import Yum
from chibi_command.echo import cowsay
from chibi.file.temp import Chibi_temp_path
from chibi_requests import Chibi_url
from chibi_command.file import Tar
from chibi_command.echo import cowsay
from chibi_requests import Chibi_url
from chibi_command import Command
from chibi.file.snippets import cd


basic_config( 'DEBUG' )
file_check_path = Chibi_path( '~/provision_installed' )
file_check = file_check_path.open()

taskwarrior_url = Chibi_url(
    'https://github.com/GothenburgBitFactory/taskwarrior/releases/'
    'download/v2.6.2/task-2.6.2.tar.gz' )

tar_extraction_dir = Chibi_path( '/chibi/.cache/waifus/pgk/' )


version_to_check = "taskwarrior\n".format( file=__file__, )


if __name__ == "__main__" and not version_to_check in file_check:
    cowsay( "instalado taskwarrior" )

    Dnf.install( 'cmake', 'gnutls' )

    download_path = Chibi_temp_path()
    taskwarrior_path = taskwarrior_url.download( download_path )

    if not tar_extraction_dir.exists:
        tar_extraction_dir.mkdir()

    tar = Tar.verbose().extract().file( taskwarrior_path )
    tar = tar.output_directory( tar_extraction_dir ).run()

    path = tar_extraction_dir + 'task-2.6.2'
    cd( path )
    result = Command(
        'cmake', '-DCMAKE_BUILD_TYPE=release', '.' ).run()
    if not result:
        raise Exception( "no se pudo usar cmake mira los logs" )
    result = Command( 'make', ).run()
    if not result:
        raise Exception( "no se pudo usar make mira los logs" )
    result = Command( 'make', 'install' ).run()
    if not result:
        raise Exception( "no se pudo usar make install mira los logs" )

    cowsay( "termino de instalar taskwarrior" )
    file_check.append( version_to_check )
