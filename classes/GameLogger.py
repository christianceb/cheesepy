from classes.Logger import Logger
from classes.Board import Board
from classes.Visualiser import Visualiser


class GameLogger:
    def __init__(self):
        self.logger = Logger()

    def state_to_file(self, board: Board):
        """
        Persist current state to file in logger

        :param board: The current game board
        :return:
        """
        self.logger.clear()
        stream = self.logger.stream()

        char_offset = 5

        # Sort pieces nicely by camo and valuation
        [white, black] = self.group_by_camo(board.pieces)

        # Set seek column number
        col = 0

        for camo in [white, black]:
            # Set preface text to clearly indicate which camo the following pieces are
            preface = " (by valuation): "
            preface = ("White" if camo[0].is_white() else "Black") + preface
            stream.write(preface)
            col += len(preface)  # Increment col to take into account recently printed text

            for piece in self.sort_by_rank(camo):
                [x, y] = piece.get_pos()
                algebraic_pos = Visualiser.to_algebraic(*[x, y])
                string = piece.name.strip() + "=" + algebraic_pos  # Format name and algebraic position nicely

                stream.write(string.ljust(char_offset))
                stream.seek(col)  # Jump to next available printable area

                col += char_offset

            # Space out next columns to make way for next camo
            stream.write(" ".ljust(char_offset-1))
            col += char_offset-1

    @staticmethod
    def group_by_camo(pieces):
        """
        Group pieces by camo(uflage)

        :param pieces:
        :return: List containing the pieces. First array contains white pieces, black on the other
        """
        camos = [[], []]

        for piece in pieces:
            camo = 0 if piece.is_white() else 1

            camos[camo].append(piece)

        return camos

    @staticmethod
    def sort_by_rank(pieces):
        """
        Sort pieces by their valuations (rank)

        :param pieces:
        :return: Pieces sorted by valuation
        """
        return sorted(pieces, key=lambda piece: piece.value)