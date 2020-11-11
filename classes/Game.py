from classes.Visualiser import Visualiser
from classes.Board import Board
from classes.MoveStatus import MoveStatus
from classes.GameLogger import GameLogger


class Game:
    __white_turn = True
    __dimensions = 8
    __castling_moves = ["O-O", "O-O-O"]

    def __init__(self):
        self.visualiser = Visualiser()
        self.board = Board()
        self.__game_logger = GameLogger()

    def visualise(self):
        """
        Visualise the board in console. No budget for a 3D cheeseboard here, a charcuterie might be cheaper

        :return: void
        """
        self.visualiser.print(self.board)

    def persist_state_to_file(self):
        self.__game_logger.state_to_file(self.board)

    def move(self, origin, destination=None):
        """
        Move the piece if it is valid

        :param origin:
        :param destination:
        :return: the result of the move
        """

        result = None

        # Filter out non-standard moves except castling
        if destination is None and origin not in self.__castling_moves:
            return MoveStatus.ERR_UNRECOGNISED

        if origin in self.__castling_moves:
            castle_result = self.board.castle(self.__white_turn, True if origin == "O-O" else False)

            if castle_result is MoveStatus.OK_CASTLED:
                # Invert current turn if move was successful
                self.__white_turn = not self.__white_turn

            result = castle_result
        else:
            # Convert atlas coordinates to cartesian coordinates
            cartesian_origin = self.atlas_to_cartesian_coordinates(origin)
            cartesian_destination = self.atlas_to_cartesian_coordinates(destination)

            move = self.board.move(*cartesian_origin, *cartesian_destination, self.__white_turn)

            if move.value > 0:
                # Invert current turn if move was successful
                self.__white_turn = not self.__white_turn

            result = move

        if result.value > 0:
            separator = "-" if result is not MoveStatus.OK_KILL else "x"

            final_destination = separator + destination if destination is not None else ""

        return result

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
