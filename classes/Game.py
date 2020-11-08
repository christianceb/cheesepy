from classes.Visualiser import Visualiser
from classes.Board import Board


class Game:
    def __init__(self):
        self.visualiser = Visualiser()
        self.board = Board()

    def visualise(self):
        """
        Visualise the board in console. No budget for a 3D cheeseboard here, a charcuterie might be cheaper

        :return: void
        """
        self.visualiser.print(self.board)

    def move(self, origin, destination):
        """
        Move the piece if it is valid

        :param origin:
        :param destination:
        :return: the result of the move
        """

        # Convert atlas coordinates to cartesian coordinates
        origin = self.atlas_to_cartesian_coordinates(origin)
        destination = self.atlas_to_cartesian_coordinates(destination)

        return self.board.move(*origin, *destination)

    def atlas_to_cartesian_coordinates(self, cell):
        """
        Convert atlas grid coordinate to cartesian coordinates

        :param cell: Cell coordinates to translate
        :return: List consisting of x and y coordinates
        """
        cell = list(cell)

        cell[0] = self.translate_a(cell[0])
        cell[1] = int(cell[1]) - 1

        return cell

    def translate_a(self, letter):
        """
        Translate atlas coordinate alphabet to its zero-indexed numeric value
        :param letter: letter to translate
        :return: integer
        """
        return self.visualiser.coordinate_map.index(letter.lower())
