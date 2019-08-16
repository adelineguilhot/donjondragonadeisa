from ..src.game.game_map import Map
from ..src.game.enemy import Enemy
from ..src.game.box import Box


def test_map_get_name():
    game_map = Map(name="Choco Island", number_of_case=64)
    assert game_map.get_name() == "Choco Island"


def test_map_get_number_of_case():
    game_map = Map(name="Choco Island", number_of_case=64)
    assert game_map.get_number_of_case() == 64


def test_map_get_case_content():
    """test si il y a un ennemi"""
    gobelin = Enemy(name="gobelin", image=":japanese_goblin:", life=6, attack=1, case_fix=2)
    box_bow = Box(name="bow", image=":bow_and_arrow:", attack=5, case_fix=3)
    game_map = Map(name="Choco Island", number_of_case=64, enemies=[gobelin], boxes=[box_bow])
    assert game_map.get_case_content(0) == 'une case vide'
    assert type(game_map.get_case_content(0) == str)
    assert game_map.get_case_content(1) == "{}, {}, attack points {}"\
        .format(gobelin.get_name(), gobelin.get_image(), gobelin.get_attack_level())
    assert game_map.get_case_content(2) == "{}, {}, attack points {}"\
        .format(box_bow.get_name(), box_bow.get_image(), box_bow.get_attack_level())













