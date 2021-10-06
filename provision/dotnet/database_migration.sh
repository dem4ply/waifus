#!/bin/bash
cowsay "Start Database Migration of $1"
cd $1
dotnet ef database update
cowsay "End Database Migration $1"
