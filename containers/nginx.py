from .base import Centos_7


class Nginx( Centos_7 ):
    scripts = (
        "nginx/install.py",
        "nginx/start.py",
        "elasticsearch/beat/filebeat_install.py",
        "elasticsearch/beat/filebeat_nginx.py",
        ( "systemd/systemd.py", 'start', 'filebeat.service' )
    )


class Ikaros( Nginx ):
    hosts = ( 'waifus', 'kibana' )


class Astraea( Nginx ):
    pass


class Caos( Nginx ):
    pass


class Nymph( Nginx ):
    pass
