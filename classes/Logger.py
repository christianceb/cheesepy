class Logger:
    def __init__(self):
        self.__file = open("log.txt", 'w+')

    def log(self, value):
        self.__file.write(value + "\n")

    def stream(self):
        return self.__file

    def clear(self):
        self.__file.truncate(0)
        self.__file.seek(0)
