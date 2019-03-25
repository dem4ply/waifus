#!/usr/bin/env python3
from chibi.command import git
from chibi.command.echo import cowsay
from chibi.file.snippets import inflate_dir, cd
from chibi.file import Chibi_file


file_check_path = inflate_dir( '~/provision_installed' )
file_check = Chibi_file( file_check_path )


version_to_check = "elixir\n".format( file=__file__, )


if __name__ == "__main__" and not version_to_check in file_check:
    cowsay( "instalando elixir" )

    git.clone(
        "https://github.com/elixir-lang/elixir.git", dest='/tmp/elixir' )
    cd( '/tmp/elixir' )
