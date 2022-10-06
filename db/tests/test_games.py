import db.games as gm
import pytest

def test_get_char_types():
    gms = gm.get_games()
    assert isinstance(gms, list)
    assert len(gms) > 1

def test_get_char_type_details():
    gm_dets = gm.get_game_details(gm.TEST_GAME_NAME)
    assert isinstance(gm_dets, dict)

def test_add_wrong_name_type():
    with pytest.raises(TypeError):
        gm.add_game('a new game',{})

def test_add_wrong_details_type():
    with pytest.raises(TypeError):
        gm.add_game('a new game',[])

def test_add_missing_field():
    with pytest.raises(ValueError):
        gm.add_game('a new game',{'foo':'bar'})

def test_add_game():
    details = {}
    for field in gm.REQUIRED_FLDS:
        details[field] = 2
    gm.add_game(gm.TEST_GAME_NAME,details)
    assert gm.game_exists(gm.TEST_GAME_NAME)