from .base import Centos_7


class Nginx( Centos_7 ):
    scripts = (
        "nginx/install.py",
        "nginx/start.py",
    )


class Ikaros( Nginx ):
    extra_hosts = (
        'kibana', 'waifus', 'sigrha.com.mx',
        'api.sigrha.client.aptude.com' )


class Astraea( Nginx ):
    pass


class Caos( Nginx ):
    pass


class Nymph( Nginx ):
    pass
