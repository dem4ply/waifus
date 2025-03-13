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


version_to_check = "rabbitmq\n".format( file=__file__, )


if __name__ == "__main__" and not version_to_check in file_check:
    cowsay( "instalando rabbitmq" )
    RPM.rpm_import(
        'https://github.com/rabbitmq/signing-keys/releases/download/3.0/'
        'rabbitmq-release-signing-key.asc' )
    RPM.rpm_import(
        'https://github.com/rabbitmq/signing-keys/releases/download/3.0/'
        'cloudsmith.rabbitmq-erlang.E495BB49CC4BBE5B.key' )
    RPM.rpm_import(
        'https://github.com/rabbitmq/signing-keys/releases/download/3.0/'
        'cloudsmith.rabbitmq-server.9F4587F226208342.key' )
    download_path = Chibi_temp_path()
    # rebbitmq_rpm = Chibi_url(
    #    "https://www.rabbitmq.com/releases/rabbitmq-server/v3.6.1/"
    #    "rabbitmq-server-3.6.1-1.noarch.rpm" ).download( path=download_path )

    Dnf.install( 'socat', 'logrotate', 'erlang', 'rabbitmq-server' )
    # Yum.local_install( rebbitmq_rpm )

    """
    Systemctl.enable( 'firewalld' ).run()
    Systemctl.start( 'firewalld' ).run()

    ports = [ "8883", "61613-61614", "15672", "5671-5672", "25672", "4369" ]
    for port in ports:
        Firewall_cmd.add_port( ports=port ).run()
    Firewall_cmd.reload()
    """

    Command( 'setsebool', "-P", "nis_enabled", "1" )
    Systemctl.enable( 'rabbitmq-server' ).run()
    Systemctl.start( 'rabbitmq-server' ).run()

    file_check.append( version_to_check )

    cowsay( "termino de instalar rabbitmq" )
