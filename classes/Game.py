from classes.Visualiser import Visualiser
from classes.Board import Board


class Game:
    __white_turn = True
    __dimensions = 8

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

        move = self.board.move(*origin, *destination, self.__white_turn)

        if move.value > 0:
            # Invert current turn if move was successful
            self.__white_turn = not self.__white_turn

        return move

    def atlas_to_cartesian_coordinates(self, cell):
        """
        Convert atlas grid coordinate to cartesian coordinates

        :param cell: Cell coordinates to translate
        :return: List consisting of x and y coordinates
        """
        cell = list(cell)

        cell[0] = self.translate_a(cell[0])  # X
        cell[1] = abs(int(cell[1]) - self.__dimensions)  # Y

        return cell

    def translate_a(self, letter):
        """
        Translate a(tlas) coordinate alphabet to its zero-indexed numeric value
        :param letter: letter to translate
        :return: integer
        """
        return self.visualiser.coordinate_map.index(letter.lower())
