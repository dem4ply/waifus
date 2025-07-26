from ..base import Rocky
from . import Django


class Chibi_datahouse( Django ):
    mounts = [
        ( "/home/$USER/mount/chibi_datahouse/"
            " home/chibi/projects/chibi_datahouse"
            " none bind,create=dir 0 0" ),
    ]

    scripts = (
        ( 'django/install_dependencies.py',
            "home/chibi/projects/chibi_datahouse" ),
        ( 'django/celery_provision.py', ),
        ( 'systemd/cp.py', 'chibi_datahouse/gunicorn.service' ),

        ( 'systemd/systemd.py', 'restart', 'gunicorn.service' ),
        ( 'systemd/systemd.py', 'enable', 'gunicorn.service' ),

        ( 'systemd/cp.py', 'chibi_datahouse/celery.service' ),
        ( 'systemd/systemd.py', 'restart', 'celery.service' ),
        ( 'systemd/systemd.py', 'enable', 'celery.service' ),

        ( 'systemd/cp.py', 'chibi_datahouse/celery_beat.service' ),
        ( 'systemd/systemd.py', 'restart', 'celery_beat.service' ),
        ( 'systemd/systemd.py', 'enable', 'celery_beat.service' ),
    )
