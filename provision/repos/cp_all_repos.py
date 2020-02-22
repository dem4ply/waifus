#!/usr/bin/env python3
import os

from chibi.command.echo import cowsay
from chibi.file import Chibi_path


provision_folder = Chibi_path( os.environ[ 'PROVISION_PATH' ] )

directory_of_repos = provision_folder + 'repos/*'
destiny_of_repos = Chibi_path( '/etc/yum.repos.d' )

cowsay( "starting to copy repos" )
directory_of_repos.copy( destiny_of_repos, verbose=True )
cowsay( "ending to copy repos" )
