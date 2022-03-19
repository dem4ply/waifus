from .base import Rocky


class Maria( Rocky ):
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
