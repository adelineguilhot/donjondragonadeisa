from .base import Person


class Enemy(Person):
    """
           This interface contains all data needed by the client about the hero
        """
    def __init__(self, name, image, life, attack, case_fix):
        Person.__init__(self, name, image, life, attack)
        self.case_fix = case_fix


    @classmethod
    def get_enemies(cls):
        list_enemies = []
        case_fix_gobelin = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
        for position_gobelin in case_fix_gobelin:
            gobelin = cls(name="gobelin", image=":japanese_goblin:", life=6, attack=1,
                          case_fix=position_gobelin - 1)
            list_enemies.append(gobelin)

        case_fix_sorcerer = [10, 20, 25, 32, 35, 36, 37, 40, 44, 47]
        for position_sorcerer in case_fix_sorcerer:
            sorcerer = cls(name="sorcerer", image=":man_mage:", life=9, attack=2,
                           case_fix=position_sorcerer - 1)
            list_enemies.append(sorcerer)

        case_fix_dragon = [45, 52, 56, 62]
        for position_dragon in case_fix_dragon:
            dragon = cls(name="dragon", image=":dragon::", life=15, attack=4,
                         case_fix=position_dragon - 1)
            list_enemies.append(dragon)

            return list_enemies


