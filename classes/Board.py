from classes.Piece import Piece


class Board:
    pieces = []

    def __init__(self):
        self.__build_starting_pieces()

    def __build_starting_pieces(self):
        self.pieces.append(Piece(*[0, 0]))

    def who_is_in(self, x, y):
        """
        Return who is in position given.

        :param x: horizontal position
        :param y: vertical position
        :return: the piece in the coordinate. None otherwise
        """

        for piece in self.pieces:
            if piece.is_in(*[x, y]):
                return piece

        return None
