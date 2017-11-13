from chibi.command import yum
from chibi.file import inflate_dir, Chibi_file


file_check_path = inflate_dir( '~/provision_installed' )
file_check = Chibi_file( file_check_path )


version_to_check = "{file}\n".format( file=__file__ )


if __name__ == "__main__" and not version_to_check in file_check:
    yum.update()
    yum.install( 'epel-release' )
    file_check.append( version_to_check )
