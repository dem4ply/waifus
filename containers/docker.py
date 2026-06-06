from .base import Rocky, Archlinux


class Docker( Archlinux ):
    scripts = (
        'docker/install.py'
    )


class Jelly( Docker ):
    pass
