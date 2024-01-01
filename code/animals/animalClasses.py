import shortuuid as uuid


class Animal:

    def __init__(self, name: str, birthday: str, executed_commands: str):
        self.__id = uuid.ShortUUID().random(length=3)
        self.__name = name
        self.__birthday = birthday
        self.__executed_commands = executed_commands
        self.__animal_type_name = "animal"

    def __str__(self) -> str:
        return f"\nID: {self.__id}\nname: {self.__name}\nbirthday: {self.__birthday}\ncommands: {self.__executed_commands}\nThis animal is {self.__animal_type_name}"

    def getName(self):
        return self.__name

    def getID(self):
        return self.__id

    def getBirthday(self):
        return self.__birthday

    def getCommands(self):
        return self.__executed_commands

    def setCommands(self, new_commands: str):
        self.__executed_commands = new_commands

    def getType(self):
        return self.__animal_type_name

    def setType(self, new_type_name):
        self.__animal_type_name = new_type_name


class Pet(Animal):
    def __init__(self, name: str, birthday: str, executed_commands: str):
        super().__init__(name, birthday, executed_commands)


class PackAnimal(Animal):

    def __init__(self, name: str, birthday: str, executed_commands: str):
        super().__init__(name, birthday, executed_commands)


class Cat(Pet):
    def __init__(self, name: str, birthday: str, executed_commands: str):
        super().__init__(name, birthday, executed_commands)
        self.animal_type_name = "cat"


class Dog(Pet):
    def __init__(self, name: str, birthday: str, executed_commands: str):
        super().__init__(name, birthday, executed_commands)
        self.animal_type_name = "dog"


class Hamster(Pet):
    def __init__(self, name: str, birthday: str, executed_commands: str):
        super().__init__(name, birthday, executed_commands)
        self.animal_type_name = "hamster"


class Donkey(PackAnimal):
    def __init__(self, name: str, birthday: str, executed_commands: str):
        super().__init__(name, birthday, executed_commands)
        self.animal_type_name = "donkey"


class Horse(PackAnimal):
    def __init__(self, name: str, birthday: str, executed_commands: str):
        super().__init__(name, birthday, executed_commands)
        self.animal_id_in_type = "horse"


class Camel(PackAnimal):
    def __init__(self, name: str, birthday: str, executed_commands: str):
        super().__init__(name, birthday, executed_commands)
        self.animal_id_in_type = "camel"
