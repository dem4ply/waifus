#!/bin/bash
cowsay "Copiando hosts"

FOLDER_PROVISION="/home/vagrant/provision"
sudo cp $FOLDER_PROVISION/hosts /etc/hosts

cowsay "Terminando de copiar host"
