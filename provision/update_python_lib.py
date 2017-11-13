from chibi.command import git, echo, pip
from chibi.file import inflate_dir, Chibi_file, ls_only_dir, join


python_lib_dir = inflate_dir( '~/python_lib' )
file_check_path = inflate_dir( '~/provision_installed' )
file_check = Chibi_file( file_check_path )

if __name__ == "__main__":
    echo.echo( '======================================================' )
    echo.echo( 'iniciando actualizacion de librerias de python locales' )
    echo.echo( '======================================================' )
    root_dir = inflate_dir( '~/python_lib' )
    libs = ls_only_dir( root_dir )
    for lib in libs:
        lib_dir = join( root_dir, lib )
        git.pull( lib_dir )
        pip.upgrade( lib_dir )

    echo.echo( '========================================================' )
    echo.echo( 'finalizando actualizacion de librerias de python locales' )
    echo.echo( '========================================================' )
