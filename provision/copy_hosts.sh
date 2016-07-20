#!/bin/bash
echo "Copiando hosts" | ponysay

FOLDER_PROVISION="/home/vagrant/provision"
sudo cp $FOLDER_PROVISION/hosts /etc/hosts

echo "Terminando de copiar host" | ponysay
