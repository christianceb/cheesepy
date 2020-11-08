from classes.Game import Game


def main():
    the_game = Game()

    the_game.visualise()
    print(the_game.move("a1", "b1"))
    print(the_game.move("b2", "b3"))
    the_game.visualise()


if __name__ == '__main__':
    main()
