from ..base import Rocky


class Django( Rocky ):
    scripts = (
        "provision/mariadb/install_client.py",
    )


class Shiro( Django ):
    pass


class Shionji( Django ):
    pass


class Victorique( Django ):
    pass
