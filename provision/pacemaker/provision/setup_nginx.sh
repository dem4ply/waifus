cowsay "Iniciando la configuracion de pacemaker para nginx"

pcs resource create web_server ocf:heartbeat:nginx \
	configfile=/etc/nginx/nginx.conf op monitor timeout="5s" interval="5s"

pcs constraint colocation add web_server virtual_ip INFINITY
pcs constraint order virtual_ip then web_server
pcs constraint location web_server prefers Ikaros=50

cowsay "terminado la configuracion de pacemaker para nginx"
