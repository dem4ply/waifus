from .base import Centos_7


class Logstash( Centos_7 ):
    scripts = (
        "logstash/install.py",
        "logstash/provision.py",

        ( "systemd/systemd.py", 'enable', 'logstash.service' ),
        ( "systemd/systemd.py", 'restart', 'logstash.service' ),
    )


class Tohru( Logstash ):
    pass


class Kanna( Logstash ):
    pass


class Elma( Logstash ):
    pass
