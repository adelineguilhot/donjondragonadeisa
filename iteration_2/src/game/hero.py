from .base import Person


class Hero(Person):
    """
       This interface contains all data needed by the client about the hero
    """
    def __init__(self, name, image, life, attack):
        Person.__init__(self, name, image, life, attack)
