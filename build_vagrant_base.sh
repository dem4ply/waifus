rm -v base_centos_7.box base_centos_8.box
vagrant package --output base_centos_7.box
vagrant box add --force base_centos_7 base_centos_7.box
