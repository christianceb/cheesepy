class Visualiser:
    coordinate_map = ("a", "b", "c", "d", "e", "f")
    __dimensions = 6

    def __init__(self):
        self.map = []
        self.__build_map()

    def __build_map(self):
        columns = []

        for i in range(self.__dimensions):
            columns.append([])

        for i in range(self.__dimensions):
            self.map.append(columns)