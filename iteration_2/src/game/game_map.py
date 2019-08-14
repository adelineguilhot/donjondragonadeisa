from .enemy import Enemy
from .box import Box


class Map(object):
    """
    This interface contains all data needed by the client about the game map
    """
    def __init__(self, name, number_of_case, enemies, boxes):
        self.name = name
        self.number_of_case = number_of_case
        self.enemies = enemies
        self.boxes = boxes
        self.map_list = self.get_empty_map()
        for single_enemy in self.enemies:
            self.map_list[single_enemy.case_fix - 1] = single_enemy
        for single_box in self.boxes:
            self.map_list[single_box.case_fix - 1] = single_box

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
        """
        Returns:
             empty game map
        """
        empty_map = [''] * self.number_of_case

        return empty_map

    def get_case_content(self, case):

        case_content = self.map_list[case]
        if case_content == '':
            case_content = 'une case vide'
            return case_content
        else:
            case_content = "{}, {}, attack points {}".format(case_content.get_name(), case_content.get_image(), case_content.get_attack_level())
            return case_content

    @classmethod
    def get_maps(cls):

        game_map = cls(name="Choco Island", number_of_case=64,
                       enemies=Enemy.get_enemies(), boxes=Box.get_boxes())

        return [game_map]
