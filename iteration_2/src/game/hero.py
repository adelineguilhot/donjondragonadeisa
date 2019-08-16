from .base import Personnage
from .caisse_surprise import Caisse_surprise
from .warrior_api import WarriorsAPI


class Hero(Personnage):
    """
       This interface contains all data needed by the client about the hero
    """
    def __init__(self, name, image, life, attack, attack_max, life_max):
        Personnage.__init__(self, name, image, life, attack)
        self.attack_max = attack_max
        self.life_max = life_max

    def give_caisse_surprise(self, caisse_surprise):
        """
        Prend en compte les bonus
        en fonction des caractéristiques des personnages
        """

        if self.name == "warrior":
            if caisse_surprise.name in ["arc", "massue", "epee"]:
                if self.attack <= self.attack_max:
                    self.attack += caisse_surprise.attack
                else:
                    self.attack = self.attack_max
            if caisse_surprise.name in ["potion_mineure", "potion_standard", "grande_potion"]:
                if self.life <= self.life_max:
                    self.life += caisse_surprise.attack
                else:
                    self.life = self.life_max

        if self.name == "wizard":
            if caisse_surprise.name in ["eclair", "boule_de_feu"]:
                if self.attack <= self.attack_max:
                    self.attack += caisse_surprise.attack
                else:
                    self.attack = self.attack_max
            if caisse_surprise.name in ["potion_mineure", "potion_standard", "grande_potion"]:
                if self.life <= self.life_max:
                    self.life += caisse_surprise.attack
                else:
                    self.life = self.life_max
