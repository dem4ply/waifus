#!/bin/bash
cowsay "inicia la provision del con npm install en $1"
repo_folder=$1

chmod -v 755 /home/chibi
cd $repo_folder
pwd

rm -r node_modules
rm package-lock.json
npm cache clean --force
set -e 
cowsay "instalando paquetes"
npm install
npm install -g serve
set +e
cowsay "termino la provision del con npm install en $repo_folder"

cowsay "creando para producción de $repo_folder"
npm run build
cowsay "termino producción de $repo_folder"
