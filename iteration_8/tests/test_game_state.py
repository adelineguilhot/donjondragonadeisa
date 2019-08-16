from ..src.game.game_state import GameState
from ..src.game.hero import Hero
from ..src.game.game_map import Map


def test_state_get_player_name():
    warrior = Hero(name="warrior", image=":man_mage:", life=5, attack=5, max_attack=10, max_life=10)
    game_map = Map(name="Choco Island", number_of_case=64)
    nom_joueur = GameState("Toto", warrior, game_map)
    assert nom_joueur.get_player_name() == "Toto"
    player = nom_joueur.get_player_name()
    assert type(player) == str


def test_state_get_hero():
    current_hero = Hero(name="warrior", image=":man_mage:", life=5, attack=5, max_attack=10, max_life=10)
    assert current_hero.get_hero() == 'warrior'
