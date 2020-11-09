from classes.Game import Game


def main():
    the_game = Game()

    # Play a scenario (uncomment a scenario)
    castling(the_game)
    #friendly_fire(the_game)

    the_game.visualise()


def friendly_fire(the_game):
    """
    Test friendly fire. Although due to the order of the validation, ERR_COLLIDE will be returned
    :param the_game:
    :return:
    """
    print(the_game.move("a1", "b1"))


def castling(the_game):
    """
    Demo castling and capture
    :param the_game:
    :return:
    """
    prepare_for_castling(the_game)
    print(the_game.move("O-O-O"))
    print(the_game.move("O-O"))
    print(the_game.move("O-O-O"))  # Should not be able to castle
    print(the_game.move("h1", "h3"))  # capture


def prepare_for_castling(the_game):
    print(the_game.move("g1", "f3"))
    print(the_game.move("g8", "f6"))
    print(the_game.move("f1", "a6"))
    print(the_game.move("f8", "a3"))
    print(the_game.move("d1", "d4"))
    print(the_game.move("d8", "d5"))
    print(the_game.move("c1", "h6"))
    print(the_game.move("c8", "h3"))
    print(the_game.move("b1", "c3"))
    print(the_game.move("b8", "c6"))


if __name__ == '__main__':
    main()
