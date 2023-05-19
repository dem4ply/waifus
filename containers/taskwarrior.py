from .base import Rocky


class Taskwarrior( Rocky ):
    scripts = (
        'taskwarrior/install.py',
    )

class Chiri( Taskwarrior ):
    pass
