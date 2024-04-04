# Author: Joel W. Prebish
# Creation Date: 04/04/2024
'''
This file contains test cases for The Towers of Hanoi project.
Please use these tests to validate your implementation.
'''
import pytest
from stack import Stack
from hanoi import TowersOfHanoi

@pytest.fixture
def game():
    return TowersOfHanoi()

def test_initial_configuration(game):
    '''Test initial tower configuration'''
    assert len(game.left_tower) == 3, "Left tower should start with 3 rings"
    assert len(game.middle_tower) == 0, "Middle tower should start empty"
    assert len(game.right_tower) == 0, "Right tower should start empty"

def test_move_ring(game):
    '''Test moving a ring from one tower to another'''
    game.move_ring(game.left_tower, game.middle_tower)
    assert len(game.left_tower) == 2, "Left tower should have 2 rings after a move"
    assert len(game.middle_tower) == 1, "Middle tower should have 1 ring after a move"
    assert len(game.right_tower) == 0, "Right tower should remain empty after the move"

def test_invalid_move(game):
    '''Test that an invalid move does not change the towers'''
    game.move_ring(game.middle_tower, game.right_tower)
    assert len(game.left_tower) == 3, "Left tower should remain unchanged after an invalid move"
    assert len(game.middle_tower) == 0, "Middle tower should remain empty after an invalid move"
    assert len(game.right_tower) == 0, "Right tower should remain unchanged after an invalid move"

def test_game_won(game):
    '''Test the game won condition'''
    game.left_tower.clear()
    game.middle_tower.clear()
    for i in range(3, 0, -1):
        game.right_tower.push(i)
    assert game.game_won(), "The game should be won when all rings are on the right tower"

def test_game_not_won(game):
    '''Test the game not won condition'''
    assert not game.game_won(), "The game should not be won initially"
