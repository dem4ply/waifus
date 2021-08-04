from ..base import Centos_7


class Owncloud( Centos_7 ):
    scripts = (
        'php/install.py',
        'php/config_fpm.py',
        'owncloud/install.py',
    )
