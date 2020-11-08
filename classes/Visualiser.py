from classes.Board import Board


class Visualiser:
    coordinate_map = ("a", "b", "c", "d", "e", "f", "g", "h")
    __dimensions = 8

    def __init__(self):
        self.map = []
        self.__build_map()

    def __build_map(self):
        """
        Creates the array of the battlefield. Should never be used for logical operations
        :return:
        """
        columns = []

        for i in range(self.__dimensions):
            columns.append([])

        for i in range(self.__dimensions):
            self.map.append(columns)

    def print(self, board: Board):
        """
        Print the entire battlefield

        :param board: The current board in play
        :return: void
        """
        # Render first horizontal alphabetical x-axis markers
        row = ["  "]

        for x_marker in self.coordinate_map:
            row.append(" " + x_marker)

        print("".join(row))

        # Render the rest of the cheese board
        for y, y_row in enumerate(self.map):
            # Render left side row numbers
            row = [" " + str(y + 1)]

            # Render battlefield
            for x, square in enumerate(y_row):
                # Check with Board if there is a piece on this coordinate
                anybody = board.who_is_in(*[x, y])

                # Anybody out there?
                if anybody is not None:
                    # Oh hai
                    row.append(" " + anybody.name)
                else:
                    # Print a simple dot!
                    row.append(" .")

            # Print the entire row
            print("".join(row))