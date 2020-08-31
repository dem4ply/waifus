from .base import Centos_7


class Rabbit( Centos_7 ):
    scripts = (
        "rabbitmq/install.py",
        "rabbitmq/add_user.py",
    )


class Chino( Rabbit ):
    pass


class Cocoa( Rabbit ):
    pass


class Rize( Rabbit ):
    pass
