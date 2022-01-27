from .base import Centos_7


class Nginx( Centos_7 ):
    scripts = (
        "nginx/install.py",
        "nginx/provision.py",
        ( "nginx/enable.py", 'enable', 'waifus', 'kibana' ),
        ( "nginx/enable.py", 'enable', 'default' ),

        ( "systemd/systemd.py", 'enable', 'nginx.service' ),
        ( "systemd/systemd.py", 'restart', 'nginx.service' ),

        "elasticsearch/beat/filebeat_install.py",
        "elasticsearch/beat/filebeat_nginx.py",
        ( "systemd/systemd.py", 'enable', 'filebeat.service' ),
        ( "systemd/systemd.py", 'start', 'filebeat.service' )
    )


class Ikaros( Nginx ):
    extra_hosts = ( 'waifus', 'kibana' )


class Astraea( Nginx ):
    pass


class Caos( Nginx ):
    pass


class Nymph( Nginx ):
    pass
