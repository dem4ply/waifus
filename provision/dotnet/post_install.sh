#!/bin/bash
FILE_CHECK=".copy_paste_dotnet_sdk"

if [ ! -f ~/$FILE_CHECK ]
then
	cowsay "Start Post Install Script"
	cp -rv /usr/share/dotnet/sdk/ /usr/lib64/dotnet/
	dotnet tool install --global dotnet-ef --version 5.0.10
	cowsay "End Post Install Script"
fi
