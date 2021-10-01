#!/bin/bash

cowsay "Cambiando permisos al usuario"
chmod 755 /home/chibi/
cowsay "ahora tienes permisos"

set -x
cowsay "inicia la provision del con npm install en $1"
repo_folder=$1

cd $repo_folder
pwd

rm -r node_modules
rm package-lock.json
npm cache clean --force
set -e 
cowsay "instalando paquetes"
npm install

set +e
cowsay "termino la provision del con npm install en $1"
set +x

cowsay "creando para producción"
npm run build
cowsay "termino producción"
cowsay "instalando servidor"
npm install -g serve
cowsay "termino instalación de servidor"
cowsay "Corriendo en puerto 8000"
serve -s build -l 8000
