#!/usr/bin/env python3
import sys
import logging

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
logger = logging.getLogger( 'waifus.provision.django.git_clone' )
chibi_home = Chibi_path( '/home/chibi' )
projects = chibi_home + 'projects'

git_repo_url = Chibi_url( sys.argv[1] )
if len( sys.argv ) > 2:
    git_repo_branch = f'origin/{sys.argv[2]}'
    git_repo_extra_name = sys.argv[2]
else:
    git_repo_branch = None
    git_repo_extra_name = None

if len( sys.argv ) > 3:
    git_repo_extra_name = Chibi_url( sys.argv[3] )

if not git_repo_url:
    raise ValueError( "el primer parametro nesesita ser un git repo" )


if not projects.exists:
    projects.mkdir()


folder = git_repo_url.base_name.rsplit( '.git', 1 )[0]
git_folder = projects + folder
if git_repo_branch:
    if git_repo_extra_name:
        git_folder = Chibi_path( f"{git_folder}__{git_repo_extra_name}" )
    else:
        git_folder = Chibi_path( f"{git_folder}__{git_repo_branch}" )

cowsay( f"clonando {git_repo_url} en {git_folder}" )
if git_folder.exists:
    logger.info( f"repo en {git_folder}" )
    Git.checkout( branch='.', src=git_folder )
    Git.checkout_track( branch=git_repo_branch, src=git_folder )
    Git.pull( src=git_folder )
    logger.info( f"pull repo {git_folder}" )
else:
    logger.info( f"clonando {git_folder}" )
    Git.clone( git_repo_url, git_folder )
    Git.checkout_track( branch=git_repo_branch, src=git_folder )

git_folder.chown(
    user_name='chibi', group_name='chibi', recursive=True, verbose=False )

cowsay( f"termino de clonar {git_repo_url}" )
