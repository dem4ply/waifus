#!/bin/bash
set -x
cowsay "inicia la provision del con npm install en $1"
repo_folder=$1

cd $repo_folder
pwd
rm -r node_modules
rm package-lock.json
set -e
npm install
set +e
cowsay "termino la provision del con npm install en $1"
set +x
