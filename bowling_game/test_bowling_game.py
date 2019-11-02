from bowling_game import Game


def test_gutter_game():
    game = Game()

    for _ in range(20):
        game.roll(0)

    assert game.final_score() == 0


def test_all_ones():
    game = Game()

    for _ in range(20):
        game.roll(1)

    assert game.final_score() == 20
