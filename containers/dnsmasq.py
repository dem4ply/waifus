from .base import Rocky


class Dns( Rocky ):
    scripts = (
        'dnsmasq/install.py'
    )


class Shionji( Dns ):
    pass
