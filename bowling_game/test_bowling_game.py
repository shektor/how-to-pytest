from bowling_game import Game


def test_gutter_game():
    game = Game()

    for _ in range(20):
        game.roll(0)

    assert game.score() == 0
