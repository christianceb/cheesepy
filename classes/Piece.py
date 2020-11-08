import time


class Piece:
    __x = None
    __y = None
    name = "X"

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

        # See self.__str__() for how this is used
        self.__timestamp = int(time.time())

    def __str__(self):
        """
        Return the unique value of this piece. Useful for when deleting items in a list

        :return: The timestamp in a string format
        """
        return str(self.__timestamp)

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
            self.__x = x
            self.__y = y

            return True

        return False

    def validate_move(self, x, y):
        """
        Contains all move validation logic specific to this piece. No other validation should be done here
        Instead, see piece_move_validate

        :param x: The new x position
        :param y: The new y position
        :return: True if move was valid. Otherwise, false
        """
        # Determine if new position is within range (1)
        if abs(x - self.__x) in [0, 1] and abs(y - self.__y) in [0, 1]:
            return True

        return False