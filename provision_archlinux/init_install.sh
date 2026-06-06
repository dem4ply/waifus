#!/bin/bash
FILE_CHECK=".init_install"

if [ ! -f ~/$FILE_CHECK ]
then
	echo "==================="
	echo "iniciando archlinux"
	echo "==================="

	echo >>EOF
	cat << EOF > /etc/locale.conf
#LANGUAGE=es_MX:es_ES:es:en
LANG=es_MX.UTF-8
#LC_TIME=es_MX
LC_ALL=
EOF
	echo "es_MX.UTF-8 UTF-8" >> /etc/locale.gen

	locale-gen

	cat << 'EOF' > /etc/pacman.d/mirrorlist
# Canada
Server = https://mirror.allthingslinux.org/archlinux/$repo/os/$arch
Server = https://arch.mirror.winslow.cloud/$repo/os/$arch
Server = https://ca.mirrors.cicku.me/archlinux/$repo/os/$arch
Server = https://mirror.cpsc.ucalgary.ca/mirror/archlinux.org/$repo/os/$arch
Server = https://mirror.csclub.uwaterloo.ca/archlinux/$repo/os/$arch
Server = https://mirror2.evolution-host.com/archlinux/$repo/os/$arch
Server = https://mirror.franscorack.com/archlinux/$repo/os/$arch
Server = https://ca.mirror.cx/archlinux/$repo/os/$arch
Server = https://mirror.quantum5.ca/archlinux/$repo/os/$arch
Server = https://muug.ca/mirror/archlinux/$repo/os/$arch
Server = https://mirror.scd31.com/arch/$repo/os/$arch
Server = https://mirror.xenyth.net/archlinux/$repo/os/$arch

# Mexico 
Server = https://lidsol.fi-b.unam.mx/archlinux/$repo/os/$arch
Server = https://arch.jsc.mx/$repo/os/$arch
EOF


	pacman -Syu --noconfirm
	pacman-key --init
	pacman-key --populate

	pacman -Syu --noconfirm sudo git base-devel

	useradd chibi
	echo "chibi ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers
	chown chibi:chibi /home/chibi

	cd /tmp/
	git clone https://aur.archlinux.org/yay.git
	cd yay
	chown -R chibi:chibi .
	su chibi -c "makepkg -si --noconfirm"

	cd ~
	touch ~/$FILE_CHECK
	echo "=========================="
	echo "fin de iniciando archlinux"
	echo "=========================="
fi
