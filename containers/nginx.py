from .base import Centos_7


class Nginx( Centos_7 ):
    scripts = (
        "nginx/install.py",
        "nginx/start.py",
    )


class Ikaros( Nginx ):
    hosts = ( 'waifus', 'kibana' )


class Astraea( Nginx ):
    pass


class Caos( Nginx ):
    pass


class Nymph( Nginx ):
    pass
