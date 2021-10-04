#!/bin/bash
cowsay "Start Post Install Script"
cp -r /usr/share/dotnet/sdk/ /usr/lib64/dotnet/
dotnet tool install --global dotnet-ef --version 5.0.10
cowsay "End Post Install Script"