from classes.Logger import Logger
from classes.Board import Board
from classes.Visualiser import Visualiser


class GameLogger:
    """
    Hardcoded column values whose key map towards a piece's UID so we can "random" access files for "random"-ness sake
    """
    __map = [119, 124, 129, 134, 139, 144, 149, 154, 159, 164, 169, 174, 179, 184, 189, 194,  # Black pieces
             22, 27, 32, 37, 42, 47, 52, 57, 62, 67, 72, 77, 82, 87, 92, 97]  # White pieces

    def __init__(self):
        self.logger = Logger()

    def action_to_file(self, origin_piece, destination_piece=None):
        """
        Given 2 pieces, set their positions in the file

        :param origin_piece: Piece
        :param destination_piece: Piece
        :return: void
        """
        stream = self.logger.stream()
        offset = self.get_piece_offset(origin_piece)

        stream.seek(offset)
        stream.write(Visualiser.to_algebraic(*origin_piece.get_pos()))

        if destination_piece:
            """ Likely a capture here, but let's make sure it is """
            destination_piece_state = "XX"
            offset = self.get_piece_offset(destination_piece)

            if not (origin_piece.is_white() ^ destination_piece.is_white()):
                """ Highly likely castling in here. Set destination piece's state instead of marking them captured """
                destination_piece_state = Visualiser.to_algebraic(*destination_piece.get_pos())

            stream.seek(offset)
            stream.write(destination_piece_state)

        # Reset seek
        stream.seek(0)

    def get_piece_offset(self, piece):
        """
        Get our piece's column offset and take into consideration all quirks
        :param piece:
        :return:
        """

        offset = self.__map[piece.uid] + 2  # "2" is an offset from piece name and the equal sign (e.g. K=e1)

        if not piece.is_white():
            """
            Black magic voodoo caused by \n needs an offset like this even though
            file.read() wont tell you a \n exists
            """
            offset += 2

        return offset

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

                col += char_offset

            # Space out next columns to make way for next camo
            stream.write("\n")

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
