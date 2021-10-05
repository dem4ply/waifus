#!/bin/bash
cowsay "Start Database Migration of $1"
cd $1
pwd
ls
dotnet ef database update
cowsay "End Database Migration $1"
