from .base import Personnage


class Hero(Personnage):
    """
       This interface contains all data needed by the client about the hero
    """
    def __init__(self, name, image, life, attack):
        Personnage.__init__(self, name, image, life, attack)


