from classes.Visualiser import Visualiser
from classes.Board import Board
from classes.MoveStatus import MoveStatus
from classes.GameLogger import GameLogger
from classes.GameHistory import GameHistory


class Game:
    __white_turn = True
    __dimensions = 8
    __castling_moves = ["O-O", "O-O-O"]

    def __init__(self,
                 print_board_after_move=False,
                 print_move_result=False,
                 always_persist_board_state=True,
                 show_recent_moves=False):
        """
        Instantiates the game of chess. Pass parameters as needed to suit your liking

        :param print_board_after_move: False by default
        :param print_move_result: False by default
        :param always_persist_board_state: True by default
        :param show_recent_moves: False by default
        """
        self.visualiser = Visualiser()
        self.board = Board()
        self.__game_logger = GameLogger()
        self.__game_history = GameHistory()

        # Game options. Refer to variable names for the acronym meanings
        self.__pbam = print_board_after_move
        self.__pmr = print_move_result
        self.__apbs = always_persist_board_state
        self.__srm = show_recent_moves

        # Persist initial state
        if self.__apbs:
            self.persist_state_to_file()

    def visualise(self):
        """
        Visualise the board in console. No budget for a 3D cheeseboard here, a charcuterie might be cheaper

        :return: void
        """
        self.visualiser.print(self.board)

    def persist_state_to_file(self):
        self.__game_logger.state_to_file(self.board)

    def persist_move_to_file(self, origin, destination=None):
        self.__game_logger.action_to_file(origin, destination)

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
            king_side = True if origin == "O-O" else False

            if self.__apbs:
                # Get our pieces for later use before they move
                origin_piece = self.get_castling_piece()
                destination_piece = self.get_castling_piece(king_side, False)

            """ Run castling move"""
            castle_result = self.board.castle(self.__white_turn, king_side)

            if castle_result is MoveStatus.OK_CASTLED:
                # Invert current turn if move was successful
                self.__white_turn = not self.__white_turn

            result = castle_result
        else:
            # Convert atlas coordinates to cartesian coordinates
            cartesian_origin = self.atlas_to_cartesian_coordinates(origin)
            origin_piece = self.board.who_is_in(*cartesian_origin)
            cartesian_destination = self.atlas_to_cartesian_coordinates(destination)
            destination_piece = self.board.who_is_in(*cartesian_destination)

            """ Run normal actions """
            move = self.board.move(*cartesian_origin, *cartesian_destination, self.__white_turn)

            if move.value > 0:
                # Invert current turn if move was successful
                self.__white_turn = not self.__white_turn

            result = move

        if result.value > 0:
            """ Run needed subroutines if we have a successful move """
            separator = "-" if result is not MoveStatus.OK_KILL else "x"

            final_destination = separator + destination if destination is not None else ""

            # Print a shoddy chessboard as needed
            if self.__pbam:
                self.visualise()

            # Log and print this movement
            if self.__srm:
                self.__game_history.log(not self.__white_turn, origin, destination)
                self.print_recent_moves()

            # Persist file if set
            if self.__apbs:
                self.persist_move_to_file(origin_piece, destination_piece)

        # Print move result irregardless if successful or not
        if self.__pmr:
            print(result)

        # Give a nice separator if some game settings are up
        if self.__pbam or self.__pmr or self.__srm:
            print(("=" * 100) + "\n\n\n")

        return result

    def get_castling_piece(self, king_side=True, king=True):
        """
        Function to return the pieces involved when castling.

        :param king_side: Determines which matching rook to get. Has no effect if king is true
        :param king: Always returns the king unless specified
        :return: Piece either Rook or King. May return None if no piece is in position
        """
        x = 4
        y = 7 if self.__white_turn else 0

        if not king:
            """ Looking for our rook """
            x = 7 if king_side == "O-O" else 0

        return self.board.who_is_in(*[x, y])

    def print_recent_moves(self):
        """
        Print recent moves by both players in a horizontal fashion

        :return:
        """
        print('.' * 100)
        self.__game_history.nice_print_history()
        print('.' * 100)

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
