from classes.Visualiser import Visualiser
from classes.Board import Board


class Game:
    def __init__(self):
        self.visualiser = Visualiser()
        self.board = Board()

    def visualise(self):
        """
        Visualise the board in console. No budget for a 3d cheeseboard here, a charcuterie might be cheaper

        :return: void
        """
        self.visualiser.print(self.board)