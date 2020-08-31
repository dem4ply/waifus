from .base import Centos_7


class Elasticsearch( Centos_7 ):
    is_master = False
    is_data = False

    scripts = (
        'stuff/install_java.py',
        'elasticsearch/install.py',
        ( 'elasticsearch/create_config.py',
            'cls.name', 'cls.is_master', 'cls.is_data' )
    )


class Kibana( Centos_7 ):
    scripts = (
        'kibana/install.py',
        'kibana/start.py',
    )


class Misuzu( Elasticsearch ):
    is_master = True
    is_data = False


class Pitou( Elasticsearch, Kibana ):
    is_master = True
    is_data = False


class Sakura( Elasticsearch ):
    is_master = True
    is_data = True


class Rem( Elasticsearch ):
    is_master = False
    is_data = True


class Rei( Elasticsearch ):
    is_master = False
    is_data = True
