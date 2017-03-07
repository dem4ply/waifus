#!/bin/bash
cowsay "Creando bases de datos"

FOLDER_PROVISION="/home/vagrant/provision"

mysql -u root -ppassword <<-EOF
CREATE DATABASE IF NOT EXISTS mad_scientist
EOF

mysql -u root -ppassword <<-EOF
CREATE DATABASE IF NOT EXISTS mad_message
EOF

cowsay "Finalizado creacion de bases de datos"
