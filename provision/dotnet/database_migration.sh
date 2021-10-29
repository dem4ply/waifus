#!/bin/bash
set -v
cowsay "Start Database Migration of $1"
cd $1
echo "cargando variables de $2"
cat $2
export $(grep -v '^#' $2 | xargs -d '\n')
dotnet ef database update
cowsay "End Database Migration $1"
