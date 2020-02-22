#!/usr/bin/env python3
from chibi_command.centos import Yum
from chibi_command.echo import cowsay
from chibi.file.snippets import inflate_dir
from chibi.file import Chibi_file


file_check_path = inflate_dir( '~/provision_installed' )
file_check = Chibi_file( file_check_path )


version_to_check = "essential 1\n".format( file=__file__, )


if __name__ == "__main__" and not version_to_check in file_check:
    cowsay( "Starting install for essential" )
    Yum.install(
        'bash-completion', 'bash-completion-extras', 'texinfo',  'vim',
        'ruby', 'git', 'kernel-headers', 'kernel-devel', 'htop' )

    file_check.append( version_to_check )
    cowsay( "Ending install for essential" )
