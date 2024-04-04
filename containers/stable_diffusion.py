from .base import Rocky


class Stable_diffusion( Rocky ):
    scripts = (
        'python/install_39.py',
        (
            'git_clone.py',
            "https://github.com/bes-dev/stable_diffusion.openvino" ),
        (
            'python/requeriments_39.py',
            '/home/chibi/projects/stable_diffusion.openvino',
            'requirements.txt', ),
        (
            'python/pip39.py',
            'Pillow', 'pyyaml', 'sv-ttk', ),
    )


class Arte( Stable_diffusion ):
    pass
