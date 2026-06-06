#!/usr/bin/env python3
import sys
import logging
from chibi.config import basic_config
from chibi.file import Chibi_path
from chibi_command import Command, Result_error
from chibi_command.echo import cowsay
from chibi_command.archilinux import Pacman
from chibi_command.nix import Systemctl
from chibi_argsparser.common import Chibi_args
from chibi.file.other import Chibi_systemd


basic_config()
logger = logging.getLogger( "ollama.prepare" )

# parser = Chibi_args()

def install_package( name ):
    Pacman.sync().no_confirm().run( name )

"""
Environment="HOME=/var/lib/ollama"
Environment="OLLAMA_MODELS=/var/lib/ollama
"""


def main():
    result = Systemctl.status( "ollama", no_fail=True ).run()
    properties = result.result.properties
    service_path = properties.FragmentPath

    service = Chibi_path( service_path )
    if not service.exists:
        print( f"no se encontro {service}" )
    else:
        f = service.open( chibi_file_class=Chibi_systemd )
        result = f.read()
        env_vars = result.service.Environment
        has_hosts = False
        for env_var in env_vars:
            print( "envar: ", env_var )
            if 'OLLAMA_HOST' in env_var:
                has_hosts = True
                break
        if not has_hosts:
            new_host = "OLLAMA_HOST=0.0.0.0:11434"
            result.service.Environment= new_host
            f.write( result )
            Systemctl.daemon_reload().run()
            cowsay( f"se agrego {new_host}" )

if __name__ == "__main__":
    sys.exit( main() )  # pragma: no cover
