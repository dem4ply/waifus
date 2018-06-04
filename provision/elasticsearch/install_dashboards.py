from chibi.command import yum, command, systemctl
from chibi.net import download
from chibi.command.echo import cowsay
from chibi.file import inflate_dir, Chibi_file, cd


cowsay( "instalasion daskboards de kibana" )
cd( '/tmp/' )
download(
    'https://download.elastic.co/beats/dashboards/beats-dashboards-1.1.0.zip',
    file_name='beats-dashboards.zip' )

yum.install( 'unzip' )
command( 'unzip', 'beats-dashboards.zip' )
cd ( 'beats-dashboards' )
command( './load.sh', '-l', 'waifus:80' )

cowsay( "fin de instalasion de los dashboards de kibana" )
