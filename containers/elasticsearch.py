from .base import Rocky


class Elasticsearch( Rocky ):
    is_master = False
    is_data = False

    scripts = (
        'stuff/install_java.py',
        'elasticsearch/install.py',
        ( 'elasticsearch/create_config.py',
            'cls.name', 'cls.is_master', 'cls.is_data' )
    )
    status_scripts = (
        'elasticsearch/print_status.py',
    )

    mounts = [
        "/mnt/hdd/waifus/elasticsearch/ home/chibi/elasticsearch/ "
        "none bind,create=dir 0 0",
    ]


class Misuzu( Elasticsearch ):
    scripts = (
        'elasticsearch/create_certs.py',
    )

    is_master = True
    is_data = True


class Pitou( Elasticsearch ):
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
