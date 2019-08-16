from .hero import Hero
from .game_map import Map
from .game_state import GameState


class WarriorsAPI(object):
    """the Warriors Game API"""

    def get_heroes(self):
        """
        Called by the client to retrieve the list of available heroes.

        Returns
            list: the list of available heroes

        """
        """On instancie"""
        """Création d'une boite vide ou l'on peux créer des personnages"""
        warrior = Hero(name="warrior", image=":man_mage:", life=5, attack=5, max_attack=10, max_life=10)
        wizard = Hero(name="wizard", image=":elf:", life=3, attack=8, max_attack=15, max_life=6)
        list_heroes = [warrior, wizard]

        return list_heroes

    def get_maps(self):
        """
        Called by the client to retrieve the list of available maps.

        Returns
            list: the list of available maps
        """

        return Map.get_maps()

    def create_game(self, player_name, hero, map):
        """Called by the client to create a new game

        Args:
            player_name (str): the name of the player
            hero (Hero): the chosen hero for the game
            map (Map): the chosen map for the game

        Returns
            GameState: the initial game state
        """
        return GameState(player_name, hero, map)





