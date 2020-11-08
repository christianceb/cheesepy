from classes.Game import Game


def main():
    the_game = Game()

    the_game.visualise()
    the_game.move("a1", "b2")
    the_game.visualise()


if __name__ == '__main__':
    main()
