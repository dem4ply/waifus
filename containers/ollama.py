from .base import Archlinux


class Ollama( Archlinux ):
    scripts = (
        ( 'pacman.py', 'ollama', 'install' ),
        ( 'ollama/prepare.py', 'ollama', 'install' ),

        ( "systemd.py", 'enable', 'ollama.service' ),
        ( "systemd.py", 'restart', 'ollama.service' ),

        ( 'ollama/prepare_model.py', 'deepseek-r1', 'pull' ),
    )


class Melchor( Ollama ):
    pass


class Baltasar( Ollama ):
    pass


class Gaspar( Ollama ):
    pass
