#!/usr/bin/env python3
import sys

from chibi_command.nix import Systemctl
from chibi.config import basic_config


basic_config()

if sys.argv[1] == 'start':
    Systemctl.start( sys.argv[2] ).run()
if sys.argv[1] == 'enable':
    Systemctl.enable( sys.argv[2] ).run()
if sys.argv[1] == 'restart':
    Systemctl.restart( sys.argv[2] ).run()
