from chibi.command.echo import cowsay
from chibi.file import Chibi_file, join


provision_folder = '/home/vagrant/provision'
file_host = 'hosts'

dest = '/etc/hosts'

if __name__ == "__main__":
    cowsay( "copy hosts file" )
    origin_hosts = Chibi_file( join( provision_folder, file_host ) )
    origin_hosts.copy( dest )
    cowsay( "ending copy hosts file" )
