class Piece:
    __x = None
    __y = None
    __max_x = 5
    __max_y = 5

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def getPos(self):
        return [self.__x, self.__y]

    def validateMove(self, newPos):
        x = newPos[0]
        y = newPos[1]

    def outOfBounds(self, newPos):
        newX = newPos[0]
        newY = newPos[1]

        if newX < 0 or newX > self.__max_x:
            return True