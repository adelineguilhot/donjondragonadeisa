class Box(object):
    """
               This interface contains all data needed by the client about the boxe surprise
    """
    def __init__(self, name, image, attack, case_fix):
        self.name = name
        self.image = image
        self.attack = attack
        self.case_fix = case_fix

    def get_name(self):
        """
        Returns
            str: the name of the hero
        """
        return self.name

    def get_image(self):
        """
        Returns
            str: the image of the hero
        """
        return self.image

    def get_life(self):
        """
        Returns
            int: the life level of the hero
        """
        return

    def get_attack_level(self):
        """
        Returns
            int: the attack level of the hero
        """
        return self.attack

    @classmethod
    def get_boxes(cls):
        list_box = []
        case_fix_bow = [2, 11, 14, 19, 26]
        for position_case_fix_bow in case_fix_bow:
            box_bow = cls(name="swords", image=":crossed_swords:", attack=1,
                          case_fix=position_case_fix_bow - 1)
            list_box.append(box_bow)

        case_fix_sledgehammer = [5, 22, 14, 19, 26]
        for position_case_fix_sledgehammer in case_fix_sledgehammer:
            box_sledgehammer = cls(name="sledgehammer", image=":hammer_pick:", attack=3,
                                   case_fix=position_case_fix_sledgehammer - 1)
            list_box.append(box_sledgehammer)

        case_fix_swords = [42, 53]
        for position_case_fix_swords in case_fix_swords:
            box_swords = cls(name="bow", image=":bow_and_arrow:", attack=5,
                             case_fix=position_case_fix_swords - 1)
            list_box.append(box_swords)

        case_fix_eclair = [1, 4, 8, 17, 23]
        for position_case_fix_eclair in case_fix_eclair:
            box_eclair = cls(name="eclair", image=":cloud_lightning:", attack=2,
                             case_fix=position_case_fix_eclair - 1)
            list_box.append(box_eclair)

        case_fix_fireball = [48, 49]
        for position_case_fix_fireball in case_fix_fireball:
            box_fireball = cls(name="fireball", image=":fire:", attack=7,
                               case_fix=position_case_fix_fireball - 1)
            list_box.append(box_fireball)

        case_fix_minor_potion = [7, 13, 28, 29, 33]
        for position_fix_minor_position in case_fix_minor_potion:
            box_minor_potion = cls(name="minot_potion", image=":petri_dish:", attack=1,
                                   case_fix=position_fix_minor_position - 1)
            list_box.append(box_minor_potion)

        case_fix_potion = [31, 39, 43]
        for position_fix_potion in case_fix_potion:
            box_potion = cls(name="standard_potion", image=":test_tube:", attack=2,
                             case_fix=position_fix_potion - 1)
            list_box.append(box_potion)

        case_fix_big_potion = [41]
        for position_fix_big_potion in case_fix_big_potion:
            box_big_potion = cls(name="big_potion", image=":alembic:", attack=5,
                                 case_fix=position_fix_big_potion - 1)
            list_box.append(box_big_potion)

            return list_box

