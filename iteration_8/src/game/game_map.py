from .enemy import Enemy
from .caisse_surprise import Caisse_surprise


class Map(object):
    """
    This interface contains all data needed by the client about the game map
    """
    def __init__(self, name, number_of_case, enemies=None, caisses_surprise=None):
        if enemies is None:
            enemies = []
        if caisses_surprise is None:
            caisses_surprise = []
        self.name = name
        self.number_of_case = number_of_case
        self.enemies = enemies
        self.caisses_surprise = caisses_surprise
        self.map_list = self.get_empty_map()
        for enemy in self.enemies:
            self.map_list[enemy.case_fix-1] = enemy
        for caisse_surprise in self.caisses_surprise:
            self.map_list[caisse_surprise.case_fix-1] = caisse_surprise

    def get_case_content(self, case):
        """
         Affiche le contenu de la case (image, nom...)
        :param case: int, index de self.map_list
        :return: str, représentation de la case
        """
        courante_case = self.map_list[case]
        if courante_case == '':
            courante_case = 'Case vide !!!'
            return courante_case
        else:
            courante_case = "{}, {}, point(s) d'attaque {}".format(courante_case.get_name(), courante_case.get_image(),
                                            courante_case.get_attack_level())
            return courante_case

    def get_case(self, case):
        """
        Donne le contenu brut de la case (image, nom...)

        """

        return self.map_list[case]

    def get_name(self):
        """
        Returns
            str: The name of the map
        """
        return self.name

    def get_number_of_case(self):
        """
        Returns
            int: the number of case
        """
        return self.number_of_case

    def get_empty_map(self):
        """Définit un plateau vide"""

        empty_map = [''] * self.number_of_case

        return empty_map

    @classmethod
    def get_maps(cls):
        """
        Called by the client to retrieve the list of available ennemies.

        Returns
            list: the list of available ennemies

        """
        """On instancie"""
        """Création d'une boîte vide où l'on peux créer des personnages"""

        game_map = cls(name="Choco Island", number_of_case=64,
                       enemies=Enemy.get_enemies(), caisses_surprise=Caisse_surprise.get_caisses_surprise())

        return [game_map]







