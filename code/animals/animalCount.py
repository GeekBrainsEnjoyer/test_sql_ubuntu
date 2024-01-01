

class AnimalCount:
    def __init__(self):
        self.__count = 0

    def add(self):
        self.__count += 1

    def getCount(self):
        return self.__count

    def setCount(self, new_count):
        self.__count = new_count

    def __str__(self) -> str:
        return f"{self.__count}"
