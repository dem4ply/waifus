from .base import Centos_7


class Maria( Centos_7 ):
    scripts = (
        "mariadb/install.py",
        "mariadb/add_databases.py",
    )


class Chii( Maria ):
    pass


class Freya( Maria ):
    pass


class Sumomo( Maria ):
    pass
