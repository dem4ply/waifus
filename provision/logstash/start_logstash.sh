#!/bin/bash
cowsay "iniciar logstash"

FOLDER_PROVISION_REPO="/home/vagrant/provision/logstash/provision"
sudo mkdir -p /etc/logstash/patterns
cp -v $FOLDER_PROVISION_REPO/conf/* /etc/logstash/conf.d/
cp -v -r -f $FOLDER_PROVISION_REPO/patterns/* /etc/logstash/patterns/
sudo systemctl restart logstash.service

cowsay "terminar de iniciar logstash"
