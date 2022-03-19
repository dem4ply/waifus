from ..base import Rocky


class Owncloud( Rocky ):
    scripts = (
        'php/install.py',
        'php/config_fpm.py',
        'owncloud/install.py',
    )
