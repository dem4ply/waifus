from chibi_lxc import Container


class Rocky( Container ):
    name = 'rocky'
    distribution = 'rockylinux'
    arch = 'amd64'
    version = '9'
    provision_folders = {
        'scripts': 'provision'
    }
    env_vars = {
        'LC_ALL': 'es_MX.utf8'
    }
    scripts = (
        'install_python.sh',
        'update_python_lib.sh',
        'stuff/install_epel.py',
        'stuff/install_cowsay.py',
        'set_basic_centos.py',
        'update_centos.py',
        'copy_host.py',
        'stuff/install_essential.py',
        'stuff/install_ponysay.py',
        'repos/cp_all_repos.py',
        ( 'add_user.py', 'chibi', )
    )
