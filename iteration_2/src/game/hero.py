from .base import Personnage


class Hero(Personnage):
    """
       This interface contains all data needed by the client about the hero
    """
    def __init__(self, name, image, life, attack, max_attack, max_life):
        Personnage.__init__(self, name, image, life, attack)
        self.max_attack = max_attack
        self.max_life = max_life

    def give_caisse_surprise_attack(self, caisse_surprise):
        """
            Prend en compte les bonus attack
            en fonction des caractéristiques des personnages
        """

        if self.name == "warrior":
            if caisse_surprise.name in ["arc", "massue", "epee"]:
                if self.attack <= self.max_attack:
                    self.attack += caisse_surprise.attack
                else:
                    self.attack = self.max_attack

        if self.name == "wizard":
            if caisse_surprise.name in ["eclair", "boule_de_feu"]:
                if self.attack <= self.max_attack:
                    self.attack += caisse_surprise.attack
                else:
                    self.attack = self.max_attack

        return self.attack

    def give_caisse_surprise_life(self, caisse_surprise):
        """
            Prend en compte les bonus attack
            en fonction des caractéristiques des personnages
        """
        if self.name == "warrior":
            if caisse_surprise.name in ["potion_mineure", "potion_standard", "grande_potion"]:
                if self.life <= self.max_life:
                    self.life += caisse_surprise.attack
                else:
                    self.life = self.max_life

        if self.name == "wizard":
            if caisse_surprise.name in ["potion_mineure", "potion_standard", "grande_potion"]:
                if self.life <= self.max_life:
                    self.life += caisse_surprise.attack
                else:
                    self.life = self.max_life

        return self.life
