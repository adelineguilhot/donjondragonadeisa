class Person(object):

    def __init__(self, name, image, life, attack):
        self.name = name
        self.image = image
        self.life = life
        self.attack = attack

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
        return self.life

    def get_attack_level(self):
        """
        Returns
            int: the attack level of the hero
        """
        return self.attack
