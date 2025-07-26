from chibi_command.echo import cowsay
from chibi.file import Chibi_path

cowsay( 'provisionando a celery' )

log_folder = Chibi_path( '/var/log/celery' )
if not log_folder.exists:
    log_folder.mkdir()

pid_folder = Chibi_path( '/var/run/celery' )
if not pid_folder.exists:
    pid_folder.mkdir()

log_folder.chown( user_name='chibi', group_name='chibi', recursive=True )
pid_folder.chown( user_name='chibi', group_name='chibi', recursive=True )

cowsay( 'termino de provisionar a celery' )
