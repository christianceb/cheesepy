import time
from math import sqrt


class Piece:
    _x = None
    _y = None
    name = "X"
    __white = True
    _collider = True
    value = 0

    def __init__(self, x, y, white=True):
        self._x = x
        self._y = y
        self.__white = white

        self.name = self.name.lower() if white else self.name.upper()
        self.name = " " + self.name

        # See self.__str__() for how this is used
        self.__timestamp = int(time.time())

    def __str__(self):
        """
        Return the unique value of this piece. Useful for when deleting items in a list

        :return: The timestamp in a string format
        """
        return str(self.__timestamp)

    def can_collide(self):
        return self._collider

    def get_pos(self):
        return [self._x, self._y]

    def is_white(self):
        return True if self.__white else False

    def is_in(self, x, y):
        """
        Is this piece in this coordinate?

        :param x:
        :param y:
        :return: True if the piece is on the provided positions
        """
        if x == self._x and y == self._y:
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
            self._x = x
            self._y = y

            self.move_hook()

            return True

        return False

    def goto_xy(self, x, y, run_hook=True):
        """
        Ignore all logic and just move the piece to the coordinates

        :param x: The new x position
        :param y: The new y position
        :param run_hook: If False, self.move_hook() will not run
        :return: void
        """
        self._x = x
        self._y = y

        if run_hook:
            self.move_hook()

    def validate_move(self, x, y):
        """
        Contains all move validation logic specific to this piece. No other validation should be done here

        :param x: The new x position
        :param y: The new y position
        :return: True if move was valid. Otherwise, false
        """
        # Determine if new position is within range (1)
        if abs(x - self._x) in [0, 1] and abs(y - self._y) in [0, 1]:
            return True

        return False

    def move_hook(self):
        """
        Override function to do additional operations in self.move() or self.goto_xy() (depending on run_hook)
        :return:
        """
        return

    def is_new_pos_linear(self, x, y):
        """
        Use the m of 2 positions to determine if it is a linear move

        :param x: New x position
        :param y: New y position
        :return: True if linear, False otherwise
        """

        # Prevent division-by-zero errors by checking for planar movement first
        if not self.is_new_pos_straight(*[x, y]):
            slope = (y - self._y) / (x - self._x)

            if slope % 1 == 0:
                return True

        return False

    def is_new_pos_straight(self, x, y):
        """
        Check if piece is moving in a straight line

        :param x: New x position
        :param y: New y position
        :return: True if moving in a straight line, False otherwise
        """
        # Straight line moves only (XOR x and y)
        if (self._x == x) ^ (self._y == y):
            return True

        return False

    def get_c(self, x, y):
        return sqrt((x - self._x) ** 2 + (y - self._y) ** 2)
