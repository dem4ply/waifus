from .base import Centos_7


class Nodejs( Centos_7 ):
    scripts = (
        'nodejs/install.sh',
        'ssh/provision.py',
        (
            'git_clone.py',
            'git@github.com:AptudeSiGRHA/sigrha-react.git', 'main' ),
        'nodejs/install.sh',
        (
            "provision/nodejs/provison_repo.sh",
            '/home/chibi/projects/sigrha-react__master' ),
        ( "systemd/cp.py", 'nodejs/sigrha_react.service' ),
        ( "systemd/systemd.py", 'enable', 'sigrha_react.service' ),
        ( "systemd/systemd.py",'start', 'sigrha_react.service' ),
    )


class Asuka( Nodejs ):
    pass
