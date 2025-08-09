from .base import Rocky


class Rabbit( Rocky ):
    scripts = (
        "rabbitmq/install.py",
        "rabbitmq/provision.py",
        "rabbitmq/add_user.py",
    )


class Chino( Rabbit ):
    pass


class Cocoa( Rabbit ):
    pass


class Rize( Rabbit ):
    pass
