class GameHistory:
    def __init__(self):
        self.history = [[], []]

    def log(self, white, origin, destination=None):
        """
        Log a given move parameter. Handles castling

        :param white: Determine whose move is this being made
        :param origin: Origin preferably in algebraic notation
        :param destination: Destination preferably in algebraic notation
        :return: void
        """
        index = 0 if white else 1

        move = origin + ("-" + destination if destination else "")

        self.history[index].append(move)

    def nice_print_history(self):
        """
        Nicely print the history into the console
        :return:
        """
        for index, camo in enumerate(self.history):
            camo_string = "White" if index == 0 else "Black"

            # So we get the most recent moves first
            camo.reverse()

            print(camo_string + ":" + ", ".join(camo))