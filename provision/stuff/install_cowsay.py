from chibi_command import echo, yum
from chibi_file import inflate_dir, Chibi_file, ls_only_dir, join, exists
from chibi_net import download

file_check_path = inflate_dir( '~/provision_installed' )
file_check = Chibi_file( file_check_path )

url_of_cowsay_rpm = (
    "http://www.melvilletheatre.com/articles/el7/"
    "cowsay-3.03-14.el7.centos.noarch.rpm"
)

cache_directory = inflate_dir( '~/.cache/' )
full_path_cowsay_rpm = join( cache_directory, 'cowsay.rpm' )


if __name__ == "__main__":
    echo.echo( '===============================' )
    echo.echo( 'iniciando instalacion de cowsay' )
    echo.echo( '===============================' )

    if not exists( full_path_cowsay_rpm ):
        download( url_of_cowsay_rpm,
                  directory=cache_directory,
                  file_name='cowsay.rpm' )
    else:
        echo.echo( "usando el cache para instalar cowsay" )

    yum.local_install( full_path_cowsay_rpm )

    echo.cowsay( 'finalizando instalacion de cowsay' )
