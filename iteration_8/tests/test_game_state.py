from ..src.game.game_state import GameState


def test_state_get_player_name():
    name_joueur = GameState(player_name="", hero="wizard", map="Choco Island")
    assert name_joueur.get_player_name() == ""
