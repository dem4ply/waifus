#!/bin/bash
cowsay "iniciar logstash"

FOLDER_PROVISION_REPO="/home/vagrant/provision/logstash/provision"

#cp -v $FOLDER_PROVISION_REPO/logstash_chilo.service /etc/systemd/system/
#systemctl stop logstash
systemctl enable logstash
#systemctl enable logstash_chilo.service

sudo mkdir -p /etc/logstash/patterns
cp -v $FOLDER_PROVISION_REPO/conf/* /etc/logstash/conf.d/
cp -v -r -f $FOLDER_PROVISION_REPO/patterns/* /etc/logstash/patterns/
systemctl restart logstash.service
#systemctl restart logstash_chilo.service

cowsay "terminar de iniciar logstash"
