#!/usr/bin/env python3
import os

from chibi.command.echo import cowsay
from chibi.file import Chibi_path


provision_folder = Chibi_path( os.environ[ 'PROVISION_PATH' ] )

directory_of_repos = provision_folder + 'repos/*'
destiny_of_repos = Chibi_path( '/etc/yum.repos.d' )

cowsay( "starting to copy repos" )
directory_of_repos.copy( destiny_of_repos, verbose=True )

origin_ls = set( a.base_name for a in directory_of_repos.ls() )
dest_ls = set( a.base_name for a in destiny_of_repos.ls() )

assert (
    origin_ls.intersection( dest_ls ) == origin_ls,
    f"no se encontraron todos los repos en el destino"
    f"{origin_ls.intersection( dest_ls )}" )
cowsay( "ending to copy repos" )
