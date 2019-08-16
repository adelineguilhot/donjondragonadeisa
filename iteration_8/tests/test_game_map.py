from ..src.game.game_map import Map
from ..src.game.enemy import Enemy
from ..src.game.caisse_surprise import Caisse_surprise


def test_map_get_name():
    game_map = Map(name="Choco Island", number_of_case=64)
    assert game_map.get_name() == "Choco Island"


def test_map_get_number_of_case():
    game_map = Map(name="Choco Island", number_of_case=64)
    assert game_map.get_number_of_case() == 64


def test_map_get_case_content():
    arc = Caisse_surprise(name="arc", image=":bow_and_arrow:", attack=1, case_fix=3)
    dragon = Enemy(name="dragon", image=":dragon::", life=15, attack=4, case_fix=2)
    game_map = Map(name="Choco Island", number_of_case=64, enemies=[dragon], caisses_surprise=[arc])
    #game_map = Map(name="Choco Island", number_of_case=64, caisses_surprise=[arc])
    assert type(game_map.get_case_content(0)) == str
    assert game_map.get_case_content(0) == 'Case vide !!!'
    dragon_str = "{}, {}, point(s) d'attaque {}".format(dragon.get_name(), dragon.get_image(),
                                           dragon.get_attack_level())
    assert game_map.get_case_content(1) == dragon_str
    arc_str = "{}, {}, point(s) d'attaque {}".format(arc.get_name(), arc.get_image(),
                                            arc.get_attack_level())
    assert game_map.get_case_content(2) == arc_str
