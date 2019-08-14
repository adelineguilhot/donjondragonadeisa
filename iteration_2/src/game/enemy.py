from .base import Personnage


class Enemy(Personnage):
    """
           This interface contains all data needed by the client about the ennemy
    """
    def __init__(self, name, image, life, attack, case_fix):
        Personnage.__init__(self, name, image, life, attack)
        self.case_fix = case_fix


    @classmethod
    def get_enemies(cls):
        list_enemies = []
        position_dragon = [45, 52, 56, 62]
        for position in position_dragon:
            dragon = cls(name="dragon", image=":dragon::", life=15, attack=4, case_fix=position)
            list_enemies.append(dragon)

        position_sorcier = [10, 20, 25, 32, 35, 36, 37, 40, 44, 47]
        for position in position_sorcier:
            sorcier = cls(name="sorcier", image=":man_mage:", life=9, attack=2, case_fix=position)
            list_enemies.append(sorcier)

        position_gobelin = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
        for position in position_gobelin:
            gobelin = cls(name="gobelin", image=":japanese_goblin:", life=6, attack=1, case_fix=position)
            list_enemies.append(gobelin)

        return list_enemies