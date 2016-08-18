FILE_CHECK=".install_pacemaker"

if [ ! -f ~/$FILE_CHECK ]
then

	cowsay "Instalado pacemaker"

	sudo yum install pcs fence-agents-all

	touch ~/$FILE_CHECK
	cowsay "fin de instalacion de pacemaker"
fi
