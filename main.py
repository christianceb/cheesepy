from classes.Game import Game


def main():
    the_game = Game()

    prepare_for_castling(the_game)
    print(the_game.move("O-O-O"))
    print(the_game.move("O-O"))
    print(the_game.move("O-O-O"))

    the_game.visualise()


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
