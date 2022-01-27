#!/usr/bin/env python3
from chibi.config import basic_config
from chibi.file import Chibi_path
from chibi_command.centos import Yum
from chibi_command.echo import cowsay


basic_config()
file_check_path = Chibi_path( '~/provision_installed' )
file_check = file_check_path.open()


version_to_check = "file beat\n".format( file=__file__, )


if __name__ == "__main__" and not version_to_check in file_check:
    cowsay( "Starting install for filebeat" )

    result = Yum.install( 'filebeat' )
    if not result:
        raise Exception(
            f"no se puedo instalar elasticsearch {vars(result)}" )

    file_check.append( version_to_check )
    cowsay( "Ending install for filebeat" )
