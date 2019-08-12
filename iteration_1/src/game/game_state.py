# '--------------------------------"""CURRENT GAME"""'----------------------------------------'
import random


class GameState(object):
    """
    This interface describes the game state which should be return after each game turn
    """
    def __init__(self, player_name, hero, map):
        self.player_name = player_name
        self.hero = hero
        self.map = map
        self.current_case = 0
        self.lancer_de = None
        self.game_status = "IN_PROGRESS"

    def get_player_name(self):
        """
        Returns:
            str: The player name
        """
        return self.player_name

    def get_game_id(self):
        """
        Returns:
            int: the game unique ID
        """
        return

    def get_game_status(self):
        """
        Returns:
            str: the game status
        """
        return self.game_status

    def get_hero(self):
        """
        Returns:
            Hero: the current hero
        """
        return self.hero

    def get_map(self):
        """
        Returns:
            Map: the current map

        """
        return self.map

    def get_last_log(self):
        """
        Returns:
            str: the last log of the game. This log is displayed by the client after each game turn
        """
        return self.current_case

    def get_current_case(self):
        """
        Returns:
            int: the current case index (base 1)
        """
        return self.current_case

    def next_turn(self):
        """
        Called by the client to execute a new turn in the game.

        Returns:
            bool: True if the move can be execute, False if move is impossible

        """
        self.lancer_de = random.randint(1, 6)
        self.current_case += self.lancer_de
        if self.current_case >= self.get_map().number_of_case:
            self.game_status = "FINISHED"
            return False
        else:
            return True
