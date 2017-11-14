from chibi.file import ls, copy, join
from chibi.command.echo import echo, cowsay


directory_of_repos = '/home/vagrant/provision/repos/'
desteny_of_repos = '/etc/yum.repos.d'

repos = filter( lambda x: x.endswith( '.repo' ), ls( directory_of_repos ) )
cowsay( "starting to copy repos" )
for repo in repos:
    src = join( directory_of_repos, repo )
    dest = join( desteny_of_repos, repo )
    echo( "copy {} -> {}".format( src, dest ) )
    copy( src, dest )
cowsay( "ending to copy repos" )
