from classes.Game import Game


def main():
    """
    Set your game parameters:

    print_board_after_move = False
    print_move_result = False
    always_persist_board_state = True
    show_recent_moves = False
    """
    the_game = Game(print_board_after_move=True, print_move_result=True, show_recent_moves=True)

    # Play a scenario (uncomment a scenario to play)
    vanilla_movement(the_game)
    # castling(the_game)
    # friendly_fire(the_game)


def vanilla_movement(the_game):
    """
    Very basic movement between pawns, rooks and a capture by white
    :param the_game:
    :return:
    """
    the_game.move("a2", "a3")
    the_game.move("h7", "h6")
    the_game.move("a3", "a4")
    the_game.move("h6", "h5")
    the_game.move("a1", "a3")
    the_game.move("h8", "h6")
    the_game.move("a3", "h3")
    the_game.move("h6", "a6")
    the_game.move("h3", "h5")


def friendly_fire(the_game):
    """
    Test friendly fire. Although due to the order of the validation, ERR_COLLIDE will be returned
    :param the_game:
    :return:
    """
    the_game.move("a1", "b1")


def castling(the_game):
    """
    Demo castling and capture
    :param the_game:
    :return:
    """
    prepare_for_castling(the_game)
    the_game.move("O-O-O")
    the_game.move("O-O")
    the_game.move("O-O-O")  # Should not be able to castle

    # Maneuver two knights to setup white knight for capture
    the_game.move("d2", "c4")
    the_game.move("e7", "d5")
    the_game.move("c4", "b6")


def prepare_for_castling(the_game):
    # Move all pawns 1 step forward
    the_game.move("a2", "a3")
    the_game.move("a7", "a6")
    the_game.move("b2", "b3")
    the_game.move("b7", "b6")
    the_game.move("c2", "c3")
    the_game.move("c7", "c6")
    the_game.move("d2", "d3")
    the_game.move("d7", "d6")
    the_game.move("e2", "e3")
    the_game.move("e7", "e6")
    the_game.move("f2", "f3")
    the_game.move("f7", "f6")
    the_game.move("g2", "g3")
    the_game.move("g7", "g6")
    the_game.move("h2", "h3")
    the_game.move("h7", "h6")
    the_game.move("b1", "d2")
    the_game.move("g8", "e7")
    the_game.move("c1", "b2")
    the_game.move("f8", "g7")
    the_game.move("d1", "c2")
    the_game.move("d8", "c7")
    the_game.move("f1", "g2")
    the_game.move("c8", "b7")
    the_game.move("g1", "e2")
    the_game.move("b8", "d7")


if __name__ == '__main__':
    main()
