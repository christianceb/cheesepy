from classes.Piece import Piece


class Rook(Piece):
    name = "r"
    _can_castle = True
    value = 4

    def validate_move(self, x, y):
        return self.is_new_pos_straight(*[x, y])

    def move_hook(self):
        if self._can_castle:
            self._can_castle = False

    def can_castle(self):
        return self._can_castle


class Knight(Piece):
    name = "n"
    __c = 2.23606797749979  # Constant right-triangle hypotenuse (range) for a knight
    _collider = False
    value = 2

    def validate_move(self, x, y):
        # A knight's move when graphed between points always has their c (hypotenuse) set to abs(self.__c)
        return self.__c == abs(self.get_c(*[x, y]))


class Bishop(Piece):
    name = "b"
    value = 3

    def validate_move(self, x, y):
        return self.is_new_pos_linear(*[x, y])


class Queen(Piece):
    name = "q"
    value = 5

    def validate_move(self, x, y):
        new_pos = [x, y]

        return self.is_new_pos_straight(*new_pos) ^ self.is_new_pos_linear(*new_pos)


class King(Piece):
    name = "k"
    value = 6
    __c = 1.4142135623730951  # Constant right-triangle hypotenuse (range) for a king
    _can_castle = True

    def validate_move(self, x, y):
        new_pos = [x, y]

        # Test direction first
        if self.is_new_pos_linear(*new_pos) ^ self.is_new_pos_straight(*new_pos):
            # Check if piece is moving within range
            if (self.get_c(*new_pos) == self.__c) ^ (self.get_c(*new_pos) == 1):  # 1 is our planar range
                return True

        return False

    def move_hook(self):
        if self._can_castle:
            self._can_castle = False

    def can_castle(self):
        return self._can_castle


class Pawn(Piece):
    name = "p"
    value = 1

    def validate_move(self, x, y):
        new_pos = [x, y]

        if self.get_c(*new_pos) == 1:  # 1 (square) is our planar range on this similar to a king
            return True

        return False
