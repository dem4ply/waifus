echo "iniciando de kibana" | ponysay

FOLDER_PROVISION="/home/vagrant/provision/elasticsearch/provision"

sudo cp -v -f $FOLDER_PROVISION/kibana.yml /opt/kibana/config/kibana.yml

sudo systemctl restart kibana.service

echo "fin de iniciar kibana" | ponysay
