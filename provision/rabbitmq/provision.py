#!/usr/bin/env python3
from chibi_command.rpm import RPM
from chibi_command.echo import cowsay
from chibi.config import basic_config
from chibi.file import Chibi_file, Chibi_path
from chibi.file.temp import Chibi_temp_path
from chibi_command import Command
from chibi_command.centos import Yum, Firewall_cmd, Dnf
from chibi_command.nix import Systemctl
from chibi_requests import Chibi_url


basic_config()
file_check_path = Chibi_path( '~/provision_installed' )
file_check = Chibi_file( file_check_path )


config = """
consumer_timeout = 31622400000
"""


if __name__ == "__main__":
    cowsay( "configurando rabbitmq" )

    conf_file = Chibi_path( '/etc/rabbitmq/rabbitmq.conf' )
    conf_file.open().write( config )
    Systemctl.restart( 'rabbitmq-server' ).run()

    cowsay( "termino de configurar rabbitmq" )
