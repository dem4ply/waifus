from ..base import Centos_7


class Django( Centos_7 ):
    scripts = (
        "provision/mariadb/install_client.py",
    )


class Shiro( Django ):
    pass


class Shionji( Django ):
    pass


class Victorique( Django ):
    pass
