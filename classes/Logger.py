class Logger:
    def __init__(self):
        self.__file = open("log.txt", 'w+')

    def log(self, value):
        self.__file.write( value + "\n")