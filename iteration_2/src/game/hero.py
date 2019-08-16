from .base import Person


class Hero(Person):
    """
       This interface contains all data needed by the client about the hero
    """
    def __init__(self, name, image, life, attack, max_attack, max_life):
        Person.__init__(self, name, image, life, attack)
        self.max_attack = max_attack
        self.max_life = max_life

    def give_boxes(self, box):
        """
        applique les bonus pour chaques personnages
        """
        if self.name == "warrior":
            if box.name in ["swords", "bow", "sledgehammer"]:
                if self.attack <= self.max_attack:
                    self.attack += box.attack
                else:
                    self.attack = self.max_attack
            if box.name in ["minot_potion", "standard_potion", "big_potion"]:
                self.life <= self.max_attack
                self.life += box.attack
            else:
                self.life = self.max_life

        if self.name == "wizard":
            if box.name in ["eclair", "fireball"]:
                if self.attack <= self.max_life:
                    self.attack += box.attack
                else:
                    self.attack = self.max_attack
            if box.name in ["minot_potion", "standard_potion", "big_potion"]:
                self.life <= self.max_attack
                self.life += box.attack
            else:
                self.life = self.max_life
