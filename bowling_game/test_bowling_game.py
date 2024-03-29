import pytest

from bowling_game import Game


@pytest.fixture
def game():
    return Game()


def roll_many(game, pins, number_of_times):
    for _ in range(number_of_times):
        game.roll(pins)


def roll_spare(game):
    game.roll(5)
    game.roll(5)


def roll_strike(game):
    game.roll(10)


def test_gutter_game(game):
    roll_many(game, 0, 20)

    assert game.final_score() == 0


def test_all_ones(game):
    roll_many(game, 1, 20)

    assert game.final_score() == 20


def test_one_spare(game):
    roll_spare(game)
    game.roll(3)
    roll_many(game, 0, 17)

    assert game.final_score() == 16


def test_one_strike(game):
    roll_strike(game)
    game.roll(3)
    game.roll(4)
    roll_many(game, 0, 16)

    assert game.final_score() == 24


def test_perfect_game(game):
    roll_many(game, 10, 12)

    assert game.final_score() == 300
