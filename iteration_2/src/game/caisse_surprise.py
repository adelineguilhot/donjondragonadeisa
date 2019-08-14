class Caisse_surprise(object):
    """
               This interface contains all data needed by the client about the caisse_surprise
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

    def get_attack_level(self):
        """
        Returns
            int: the attack level of the hero
        """
        return self.attack

    @classmethod
    def get_caisses_surprise(cls):
        list_caisses_surprise = []

        position_arc = [2, 11, 14, 19, 26]
        for position in position_arc:
            arc = cls(name="arc", image=":bow_and_arrow:", attack=1, case_fix=position)
            list_caisses_surprise.append(arc)

        position_massue = [5, 22, 38]
        for position in position_massue:
            massue = cls(name="massue", image=":hammer_pick:", attack=3, case_fix=position)
            list_caisses_surprise.append(massue)

        position_epee = [42, 53]
        for position in position_epee:
            epee = cls(name="epee", image=":crossed_swords:", attack=5, case_fix=position)
            list_caisses_surprise.append(epee)

        position_eclair = [1, 4, 8, 17, 23]
        for position in position_eclair:
            eclair = cls(name="eclair", image=":zap:", attack=2, case_fix=position)
            list_caisses_surprise.append(eclair)

        position_boule_de_feu = [48, 49]
        for position in position_boule_de_feu:
            boule_de_feu = cls(name="boule de feu", image=":fire:", attack=7, case_fix=position)
            list_caisses_surprise.append(boule_de_feu)

        position_potion_mineure = [7, 13, 28, 29, 33]
        for position in position_potion_mineure:
            potion_mineure = cls(name="potion mineure", image=":chocolate_bar:", attack=1,
                                             case_fix=position)
            list_caisses_surprise.append(potion_mineure)

        position_potion_standard = [31, 39, 43]
        for position in position_potion_standard:
            potion_standard = cls(name="potion standard", image=":doughnut:", attack=2, case_fix=position)
            list_caisses_surprise.append(potion_standard)

        position_grande_potion = [41]
        for position in position_grande_potion:
            grande_potion = cls(name="grande potion", image=":birthday:", attack=5, case_fix=position)
            list_caisses_surprise.append(grande_potion)

        return list_caisses_surprise