#!/bin/bash
set +e
#set +v

cowsay "Start Database Migration"
cp -r /usr/share/dotnet/sdk/ /usr/lib64/dotnet/
dotnet tool install --global dotnet-ef --version 5.0.10
cd /home/chibi/projects/clients_service/API_Clients/
dotnet ef database update

cowsay "End Database Migration" 
cowsay "DB SIGRHA_Clients created on Chii Server"
#set -v


