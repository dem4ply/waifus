cowsay "iniciando de kibana"

FOLDER_PROVISION="/home/vagrant/provision/elasticsearch/provision"

sudo cp -v -f $FOLDER_PROVISION/kibana.yml /opt/kibana/config/kibana.yml

sudo systemctl restart kibana.service

cowsay "fin de iniciar kibana"
