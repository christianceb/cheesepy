from classes.Piece import Piece


class Rook(Piece):
    name = "R"

    def validate_move(self, x, y):
        return self.is_new_pos_straight(*[x, y])


class Knight(Piece):
    name = "k"
    __c = 2.23606797749979  # Constant right-triangle hypotenuse (range) for a knight

    def validate_move(self, x, y):
        # A knight's move when graphed between points always has their c (hypotenuse) set to abs(self.__c)
        return self.__c == abs(self.get_c(*[x, y]))


class Bishop(Piece):
    name = "B"

    def validate_move(self, x, y):
        return self.is_new_pos_linear(*[x, y])


class Queen(Piece):
    name = "Q"

    def validate_move(self, x, y):
        new_pos = [x, y]

        return self.is_new_pos_straight(*new_pos) ^ self.is_new_pos_linear(*new_pos)


class King(Piece):
    name = "K"
    __c = 1.4142135623730951  # Constant right-triangle hypotenuse (range) for a king

    def validate_move(self, x, y):
        new_pos = [x, y]

        # Test direction first
        if self.is_new_pos_linear(*new_pos) ^ self.is_new_pos_straight(*new_pos):
            # Check if piece is moving within range
            if (self.get_c(*new_pos) == self.__c) ^ (self.get_c(*new_pos) == 1):  # 1 is our planar range
                return True

        return False
