#!/bin/bash
set +e
set +v
FILE_CHECK=".centos_8"

if [ ! -f ~/$FILE_CHECK ]
then
	cowsay "actualizando a centos 8"
	yum -y install epel-release
	yum -y update
	yum -y install rpmconf yum-utils

	yes N | rpmconf -a
	yum -y remove rpmconf
	package-cleanup --leaves
	package-cleanup --orphans
	yum -y install dnf
	dnf -y remove yum yum-metadata-parser
	#dnf -y install http://mirror.centos.org/centos/8/BaseOS/x86_64/os/Packages/centos-linux-repos-8-2.el8.noarch.rpm http://mirror.centos.org/centos/8/BaseOS/x86_64/os/Packages/centos-gpg-keys-8-2.el8.noarch.rpm
	dnf -y install http://mirror.centos.org/centos/8/BaseOS/x86_64/os/Packages/centos-linux-repos-8-2.el8.noarch.rpm http://mirror.centos.org/centos/8/BaseOS/x86_64/os/Packages/centos-linux-release-8.4-1.2105.el8.noarch.rpm http://mirror.centos.org/centos/8/BaseOS/x86_64/os/Packages/centos-gpg-keys-8-2.el8.noarch.rpm
	dnf -y remove python3
	sleep 3
	dnf -y update kernel
	dnf clean all
	sleep 3
	dnf -y update --best --allowerasing ebtables
	dnf -y update --best --allowerasing rpm
	dnf -y update --nobest

	#dnf -y remove  sysvinit-tools
	#dnf -y update kernel
	#dnf -y update --nobest
	#dnf -y update --nobest
	#dnf -y update --nobest
	##yum -y remove libselinux-python
	#yum -y install libselinux
	#yum -y remove newt
	#yum -y install newt

	dnf clean all

	#rm -Rf /etc/yum
	#ln -s /bin/dnf /bin/yum

	dnf -y upgrade
	#rpm -e --nodeps sysvinit-tools

	#dnf -y --releasever=8 --allowerasing --setopt=deltarpm=false distro-sync
	#cat /etc/os-release | cowsay
	#cat /etc/redhat-release | cowsay
	#uname -a | cowsay

	touch ~/$FILE_CHECK
	cowsay "termino de actulizar a centos 8"
fi
