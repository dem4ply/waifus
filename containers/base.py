from chibi_lxc import Container


class Centos_7( Container ):
    name = 'centos_7'
    distribution = 'centos'
    arch = 'amd64'
    version = '7'
    provision_folders = {
        'scripts': 'provision'
    }
    scripts = (
        'install_python.sh',
    )
