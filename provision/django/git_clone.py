#!/usr/bin/env python3
import sys

from chibi.config import basic_config
from chibi_requests import Chibi_url
from chibi.file import Chibi_path
from chibi.file.snippets import cd
from chibi_command import Command
from chibi_command.centos import Yum
from chibi_command.echo import cowsay
from chibi_command.git import Git
from git.exc import NoSuchPathError, InvalidGitRepositoryError


basic_config()
chibi_home = Chibi_path( '/home/chibi' )
projects = chibi_home + 'projects'

git_repo_url = Chibi_url( sys.argv[1] )
if not git_repo_url:
    raise ValueError( "el primer parametro nesesita ser un git repo" )


if not projects.exists:
    projects.mkdir()


folder = git_repo_url.base_name.rsplit( '.git', 1 )[0]
cowsay( f"clonando {git_repo_url}" )
git_folder = projects + folder
try:
    Git.repo( git_folder )
    Git.pull( git_folder )
except NoSuchPathError:
    Git.clone( git_repo_url, git_folder )
except InvalidGitRepositoryError:
    Git.clone( git_repo_url, git_folder )

cowsay( f"termino de clonar {git_repo_url}" )
