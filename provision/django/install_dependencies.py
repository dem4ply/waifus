import sys

from chibi.file import Chibi_path
from chibi_command import Command
from chibi_requests import Chibi_url


chibi_home = Chibi_path( '/home/chibi' )
projects = chibi_home + 'projects'

git_repo_url = Chibi_url( sys.argv[1] )
if not git_repo_url:
    raise ValueError( "el primer parametro nesesita ser un git repo" )

if not projects.exists:
    projects.mkdir()

folder = git_repo_url.base_name.rsplit( '.git', 1 )[0]
git_folder = projects + folder

requirements = git_folder + 'requirements_prod.txt'
if not requirements.exists:
    raise OSError( f'el archivo de requerimientos no existe "{requirements}"' )
Command( 'pip3', 'install', '-r', requirements ).run()
