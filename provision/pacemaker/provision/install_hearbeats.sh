cowsay "Copiando los hearbeats"

if [ ! -d ~/.cache/hearbeats ]
then
	mkdir ~/.cache/hearbeats
fi

if [ ! -f ~/.cache/hearbeats/nginx ]
then
	wget --no-cookies --no-check-certificate \
		--progress=bar:force \
		-O ~/.cache/hearbeats/nginx \
		"https://raw.githubusercontent.com/ClusterLabs/resource-agents/master/heartbeat/nginx"
fi

cp -v ~/.cache/hearbeats/* /usr/lib/ocf/resource.d/heartbeat/

cowsay "termino de copiar los hearbeats"
