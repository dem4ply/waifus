from .base import Rocky


class Kibana( Rocky ):
    scripts = (
        'kibana/install.py',
        'kibana/start.py',

        ( "systemd/systemd.py", 'enable', 'kibana.service' ),
        ( "systemd/systemd.py", 'restart', 'kibana.service' ),

    )


class Pochi( Kibana ):
    pass


class Tama( Kibana ):
    pass
