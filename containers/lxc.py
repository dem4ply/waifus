from .base import Rocky, Archlinux


class Lxc( Rocky ):
    scripts = (
        'lxc/install.py',
        'lxc/install_chibi_lxc.sh',
        ( 'git_clone.py', 'https://github.com/dem4ply/waifus.git' ),
        'lxc/provision.py',
    )


class Koko( Lxc ):
    pass


class Valmet( Lxc ):
    pass
