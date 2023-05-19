from ..base import Rocky


class Owncloud( Rocky ):
    scripts = (
        'apache/install.py',
        'php/install.py',
        'php/install_owcloud_dependencies.py',
        #'php/config_fpm.py',
        'owncloud/install.py',
        ( 'cp.py', 'apache/conf/owncloud.conf', '/etc/httpd/conf.d/' ),
        ( 'systemd/systemd.py', 'restart', 'httpd.service' ),
        ( 'systemd/systemd.py', 'enable', 'httpd.service' ),
    )

    mounts = [
        "/home/$USER/mount/owncloud/data var/www/owncloud/data/ "
        "none bind,create=dir 0 0",
    ]

class Fafnir( Owncloud ):
    pass
