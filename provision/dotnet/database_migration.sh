#!/bin/bash
set +e
#set +v

cowsay "Start Database Migration"
cd /home/chibi/projects/clients_service/API_Clients/
dotnet ef database update

cowsay "End Database Migration" 
cowsay "DB SIGRHA_Clients created on Chii Server"
#set -v


