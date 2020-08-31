#!/usr/bin/env python3
import os
import sys

from chibi.config import basic_config
from chibi.file import Chibi_path
from chibi_command.nix import Systemctl
from chibi_command.echo import cowsay


basic_config()
provision_folder = Chibi_path( os.environ[ 'PROVISION_PATH' ] )

systemd_provision = provision_folder + 'systemd'
systemd_root = Chibi_path( '/etc/systemd/system' )

target = systemd_provision + sys.argv[1]
if len( sys.argv ) > 2:
    rename = sys.argv[2]
else:
    rename = target.base_name

cowsay( f"starting to copy systemd {target.base_name}" )

envars = target.replace_extensions( 'env' )
target.copy( systemd_root + rename )
if envars.exists:
    envars.copy( systemd_root + rename.replace_extensions( 'env' ) )

Systemctl.daemon_reload().run()
cowsay( f"ending to copy systemd {target.base_name}" )
