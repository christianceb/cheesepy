from classes.Piece import Piece
from classes.Pieces import Rook, Knight, Bishop, Queen, King
from classes.MoveStatus import MoveStatus


class Board:
    pieces = []
    __boundary = 7

    def __init__(self):
        self.__build_starting_pieces()

    def __build_starting_pieces(self):
        # Black pieces
        self.pieces.append(Rook(*[0, 0], False))
        self.pieces.append(Knight(*[1, 0], False))
        self.pieces.append(Bishop(*[2, 0], False))
        self.pieces.append(Queen(*[3, 0], False))
        self.pieces.append(King(*[4, 0], False))
        self.pieces.append(Bishop(*[5, 0], False))
        self.pieces.append(Knight(*[6, 0], False))
        self.pieces.append(Rook(*[7, 4], False))

        # White pieces
        self.pieces.append(Rook(*[0, 7]))
        self.pieces.append(Knight(*[1, 7]))
        self.pieces.append(Bishop(*[2, 7]))
        self.pieces.append(Queen(*[3, 7]))
        self.pieces.append(King(*[4, 7]))
        self.pieces.append(Bishop(*[5, 7]))
        self.pieces.append(Knight(*[6, 7]))
        self.pieces.append(Rook(*[7, 7]))

        # Demo pieces
        # self.pieces.append(Piece(*[0, 0]))
        # self.pieces.append(Piece(*[1, 1], False))

    def move(self, x, y, to_x, to_y, whites_turn):
        """
        Move a piece on the board. Will test the following conditions before moving:
        1. A self-pwn
        2. Out-of-bounds test
        3. If nobody is in the origin coordinate
        4. If the move is valid based on the piece's unique movement

        Other conditions needing implementation
        1. collider
        2. castling
        3. promotion? (out of scope)

        :param x: origin row
        :param y: origin column
        :param to_x: destination row
        :param to_y: destination column
        :param whites_turn: boolean use this value to test MoveStatus.ERR_WAIT_TURN
        :return: an integer corresponding to a result
        """

        if [x, y] == [to_x, to_y]:
            return MoveStatus.ERR_SELF_PWN

        if self.out_of_bounds(*[x, y]) or self.out_of_bounds(*[x, y]):
            return MoveStatus.ERR_OOB

        piece = self.who_is_in(*[x, y])
        if piece is None:
            return MoveStatus.ERR_ENOENT

        if piece.is_white() != whites_turn:
            return MoveStatus.ERR_WAIT_TURN

        # Check if the move is legal
        if not piece.validate_move(*[to_x, to_y]):
            return MoveStatus.ERR_MOVE_ILLEGAL

        # Collider test
        if piece.can_collide() and self.has_collisions(piece, *[to_x, to_y]):
            return MoveStatus.ERR_COLLIDE

        kill = False
        target_piece = self.who_is_in(*[to_x, to_y])

        # TODO: logic for comparing against the target piece goes here
        # TODO: castling logic
        if target_piece is not None:
            if target_piece.is_white() and piece.is_white():
                return MoveStatus.ERR_FF
            else:
                self.pieces.remove(target_piece)
                kill = True

        # Finally move the piece
        piece.move(*[to_x, to_y])

        return MoveStatus.OK_KILL if kill else MoveStatus.OK_MOVE

    def has_collisions(self, piece, x, y):
        reached_destination = False
        collided = False
        x_tg, y_tg = piece.get_pos()  # tg = t(ele)g(raphed) movement
        x_direction = self.move_forward(x_tg, x)
        y_direction = self.move_forward(y_tg, y)

        while not reached_destination and not collided:
            # Offset to destination based on direction
            if x_tg != x:
                x_tg += x_direction
            if y_tg != y:
                y_tg += y_direction

            # Check for anybody in the path
            piece_in_position = self.who_is_in(*[x_tg, y_tg])

            # Collided with a piece but might not yet be the end of it
            if piece_in_position:
                if y_tg == y and x == x_tg:
                    # Collided at destination. What could it be?
                    if not (piece_in_position.is_white() ^ piece.is_white()):
                        collided = True
                else:
                    # Collided with a piece even before reaching destination
                    collided = True

            if y_tg == y and x == x_tg:
                reached_destination = True

        return collided

    @staticmethod
    def move_forward(a, b):
        delta = b - a

        if delta < 0:
            return -1
        elif delta > 0:
            return 1

        return 0

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

    def out_of_bounds(self, x, y):
        """
        Is the specified coordinate pair going to OOB our piece?

        :param x: The new x position
        :param y: The new y position
        :return: True if move was valid. Otherwise, false
        """
        if (0 <= x <= self.__boundary) or (0 <= y <= self.__boundary):
            return False

        return True
