class Piece:
    __x = None
    __y = None
    __max_x = 7
    __max_y = 7
    name = "X"

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def is_in(self, x, y):
        """
        Is this piece in this coordinate?

        :param x:
        :param y:
        :return: True if the piece is on the provided positions
        """
        if x == self.__x and y == self.__y:
            return True

        return False

    def move(self, x, y):
        """
        Moves the piece to the new position.

        :param x: The new x position
        :param y: The new y position
        :return: True if the piece was moved successfully. False if it made an illegal move
        """
        if self.validate_move(*[x, y]):
            return True

        return False

    def validate_move(self, x, y):
        """
        Contains all move validation logic. Do not write piece-specific validation here.
        Instead, see piece_move_validate

        :param x: The new x position
        :param y: The new y position
        :return: True if move was valid. Otherwise, false
        """
        valid = True

        # Simple sanity check for out of bounds
        if valid:
            valid = not self.out_of_bounds(*[x,y])

        # Piece-specific move validation
        if valid:
            valid = self.piece_move_validate(*[x,y])

        return valid

    def piece_move_validate(self, x, y):
        """
        Contains piece-specific moves (is this a valid "L" knight move? is the piece hacking?)

        :param x: The new x position
        :param y: The new y position
        :return: True if move was valid. Otherwise, false
        """
        # Determine if new position is within range (1)
        if abs(x - self.__x) in [0, 1] and abs(y - self.__y) in [0, 1]:
            return True

        return False

    def out_of_bounds(self, x, y):
        """
        Is the specified coordinate pair going to OOB our piece?

        :param x: The new x position
        :param y: The new y position
        :return: True if move was valid. Otherwise, false
        """
        if (0 <= x <= self.__max_x) or (0 <= y <= self.__max_y):
            return True

        return False
