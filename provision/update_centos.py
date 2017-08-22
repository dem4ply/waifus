import os
from chibi_command import yum


file_check = os.path.expanduser( '~/provision_installed' )


if __name__ == "__main__":
    with open( file_check ) as f:
        file_cont = f.read()
        not_need_install = __file__ in file_cont

    if not_need_install:
        pass
    else:
        yum.update()
        yum.install( 'epel-release' )
        with open( file_check, 'a' ) as f:
            f.write( __file__ + '\n' )
