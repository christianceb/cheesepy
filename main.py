from classes.Game import Game


def main():
    the_game = Game()

    # Play a scenario (uncomment a scenario)
    # castling(the_game)
    friendly_fire(the_game)

    the_game.visualise()
    the_game.persist_state_to_file()


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

    # Maneuver two knights to setup white knight for capture
    print(the_game.move("d2", "c4"))
    print(the_game.move("e7", "d5"))
    print(the_game.move("c4", "b6"))


def prepare_for_castling(the_game):
    # Move all pawns 1 step forward
    print(the_game.move("a2", "a3"))
    print(the_game.move("a7", "a6"))
    print(the_game.move("b2", "b3"))
    print(the_game.move("b7", "b6"))
    print(the_game.move("c2", "c3"))
    print(the_game.move("c7", "c6"))
    print(the_game.move("d2", "d3"))
    print(the_game.move("d7", "d6"))
    print(the_game.move("e2", "e3"))
    print(the_game.move("e7", "e6"))
    print(the_game.move("f2", "f3"))
    print(the_game.move("f7", "f6"))
    print(the_game.move("g2", "g3"))
    print(the_game.move("g7", "g6"))
    print(the_game.move("h2", "h3"))
    print(the_game.move("h7", "h6"))
    print(the_game.move("b1", "d2"))
    print(the_game.move("g8", "e7"))
    print(the_game.move("c1", "b2"))
    print(the_game.move("f8", "g7"))
    print(the_game.move("d1", "c2"))
    print(the_game.move("d8", "c7"))
    print(the_game.move("f1", "g2"))
    print(the_game.move("c8", "b7"))
    print(the_game.move("g1", "e2"))
    print(the_game.move("b8", "d7"))

if __name__ == '__main__':
    main()
