from ..base import Rocky


class Django( Rocky ):
    git_repo = None
    scripts = (
        "mariadb/install_client.py",
        ( 'git_clone.py', "cls.git_repo" ),
    )


class Corona_chan( Django ):
    git_repo = "https://github.com/dem4ply/corona_chan.git"

    scripts = (
        ( 'django/install_dependencies.py', "cls.git_repo" ),
        ( 'systemd/cp.py', 'corona_chan/gunicorn.service' ),
        ( 'systemd/systemd.py', 'restart', 'gunicorn.service' ),
        ( 'systemd/systemd.py', 'enable', 'gunicorn.service' ),
    )
