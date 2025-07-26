from ..base import Rocky


class Django( Rocky ):
    scripts = (
        "mariadb/install_client.py",
    )


class Shiro( Django ):
    pass


class Victorique( Django ):
    pass
