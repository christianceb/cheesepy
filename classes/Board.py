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
        self.pieces.append(Rook(*[7, 0], False))

        # White pieces
        self.pieces.append(Rook(*[0, 7]))
        self.pieces.append(Knight(*[1, 7]))
        self.pieces.append(Bishop(*[2, 7]))
        self.pieces.append(Queen(*[3, 7]))
        self.pieces.append(King(*[4, 7]))
        self.pieces.append(Bishop(*[5, 7]))
        self.pieces.append(Knight(*[6, 7]))
        self.pieces.append(Rook(*[7, 7]))

    def move(self, x, y, to_x, to_y, whites_turn):
        """
        Move a piece on the board. Will test a good amount of conditions prior to moving

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
        """
        Dead-reckon a piece's path and check for any collisions

        :param piece: Our piece
        :param x: destination X
        :param y: destination Y
        :return: True if there is a collision. False otherwise.
        """
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

    def castle(self, white_to_castle, king_side):
        """
        I am tired and I just want to get castling working irregardless of how WET this method becomes

        Also no collision detection so good luck implementing it later!

        :param white_to_castle:
        :param king_side:
        :return: MoveStatus
        """
        if white_to_castle:
            king = self.who_is_in(*[4, 7])

            if not isinstance(king, King) or not king.can_castle():
                return MoveStatus.ERR_CANT_CASTLE

            if king_side:
                rook = self.who_is_in(*[7, 7])

                if not isinstance(rook, Rook) or not rook.can_castle():
                    return MoveStatus.ERR_CANT_CASTLE
                else:
                    king.goto_xy(*[6, 7])
                    rook.goto_xy(*[5, 7])

                    return MoveStatus.OK_CASTLED
            else:
                rook = self.who_is_in(*[0, 7])

                if not isinstance(rook, Rook) or not rook.can_castle():
                    return MoveStatus.ERR_CANT_CASTLE
                else:
                    king.goto_xy(*[2, 7])
                    rook.goto_xy(*[3, 7])

                    return MoveStatus.OK_CASTLED
        else:
            king = self.who_is_in(*[4, 0])

            if not isinstance(king, King) or not king.can_castle():
                return MoveStatus.ERR_CANT_CASTLE

            if king_side:
                rook = self.who_is_in(*[7, 0])

                if not isinstance(rook, Rook) or not rook.can_castle():
                    return MoveStatus.ERR_CANT_CASTLE
                else:
                    king.goto_xy(*[6, 0])
                    rook.goto_xy(*[5, 0])

                    return MoveStatus.OK_CASTLED
            else:
                rook = self.who_is_in(*[0, 0])

                if not isinstance(rook, Rook) or not rook.can_castle():
                    return MoveStatus.ERR_CANT_CASTLE
                else:
                    king.goto_xy(*[2, 0])
                    rook.goto_xy(*[3, 0])

                    return MoveStatus.OK_CASTLED

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
