from abc import ABCMeta as abc


class AnimalABC(metaclass=abc):
    id = -1
    def __init__(self, name: str, birthday: str, executed_commands: str):
        self.id = -1
        self.name = name
        self.birthday = birthday
        self.executed_commands = executed_commands

    def __str__(self) -> str:
        return f"ID: {self.id}\nname: {self.name}\nbirthday: {self.birthday}\ncommands: {self.executed_commands}"

    def getName(self):
        return self.name

    def getID(self):
        return self.id

    def getBirthday(self):
        return self.birthday

    def getCommands(self):
        return self.executed_commands

    def setCommands(self, new_commands: str):
        self.executed_commands = new_commands


class Animal(AnimalABC):
    animal_id_in_type = 0

    def __init__(self, name: str, birthday: str, executed_commands: str):
        super().__init__(name, birthday, executed_commands)
        self.id = self.incr()

    def getType(self):
        return self.animal_id_in_type

    def setType(self, new_type_id):
        self.animal_id_in_type = new_type_id

    @classmethod
    def incr(self):
        self.id += 1
        return self.id


class Pet(Animal):
    def __init__(self, name: str, birthday: str, executed_commands: str):
        super().__init__(name, birthday, executed_commands)

    def __str__(self) -> str:
        return f"{super().__str__()}\nPet type ID: {self.animal_id_in_type}\n"


class PackAnimal(Animal):

    def __init__(self, name: str, birthday: str, executed_commands: str):
        super().__init__(name, birthday, executed_commands)

    def __str__(self) -> str:
        return f"{super().__str__()}\nPack animal type ID: {self.animal_id_in_type}\n"


class Cat(Pet):
    def __init__(self, name: str, birthday: str, executed_commands: str):
        super().__init__(name, birthday, executed_commands)
        self.animal_id_in_type = 1


class Dog(Pet):
    def __init__(self, name: str, birthday: str, executed_commands: str):
        super().__init__(name, birthday, executed_commands)
        self.animal_id_in_type = 2


class Hamster(Pet):
    def __init__(self, name: str, birthday: str, executed_commands: str):
        super().__init__(name, birthday, executed_commands)
        self.animal_id_in_type = 3


class Donkey(PackAnimal):
    def __init__(self, name: str, birthday: str, executed_commands: str):
        super().__init__(name, birthday, executed_commands)
        self.animal_id_in_type = 1


class Horse(PackAnimal):
    def __init__(self, name: str, birthday: str, executed_commands: str):
        super().__init__(name, birthday, executed_commands)
        self.animal_id_in_type = 2


class Camel(PackAnimal):
    def __init__(self, name: str, birthday: str, executed_commands: str):
        super().__init__(name, birthday, executed_commands)
        self.animal_id_in_type = 3
