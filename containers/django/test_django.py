from ..base import Rocky
from . import Django


class Test_django( Django ):
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
        (
            'systemd/provision_service.py',
            '--name', 'test_celery',
            '--project_name', 'chibi_test_celery',
            '-e', 'celery'
        ),

        (
            'systemd/provision/celery.py',
            '--name', 'better_celery',
            '--project_name', 'chibi_test_celery',
            '-e', 'celery'
        ),
        (
            'systemd/provision/celery.py',
            '--name', 'celery_with_queues',
            '--project_name', 'chibi_test_celery',
            '-e', 'celery',
            'example.queue', 'another.queue',
        ),
    )
