from .base import Rocky


class Maria( Rocky ):
    scripts = (
        "mariadb/install.py",
        ( "mariadb/add_database.py", 'reader_moe', ),
        ( "mariadb/add_database.py", 'test_reader_moe', ),
        ( "mariadb/add_database.py", 'corona_chan', ),
        ( "mariadb/add_database.py", 'friends_on_demand', ),
        ( "mariadb/add_database.py", 'archivum', ),
        ( "mariadb/add_database.py", 'test_archivum', ),
        ( "mariadb/add_database.py", 'owncloud_db', ),
        ( "mariadb/add_database.py", 'cab_tracking', ),
        "mariadb/add_owncloud_user.py",
    )


class Chii( Maria ):
    pass


class Freya( Maria ):
    pass


class Sumomo( Maria ):
    pass
