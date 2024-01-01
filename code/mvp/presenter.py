from animals.animalClasses import *
from mvp.model import *
from animals.animalCount import AnimalCount


class Presenter:
    def __init__(self, model=Model()) -> None:
        self.__model = model
        self.__count = AnimalCount()
        self.__count.setCount(len(self.__model.getAnimals_list()))

    def showAnimals(self):
        if len(self.__model.getAnimals_list()) == 0:
            print("\nЖивотных нет!")
        else:
            print(f"\nСписок животных:\n{self.__model}")

    def __pickAnimal(self, selected_animal: str):
        a_list = self.__model.getAnimals_list()
        for i in range(len(a_list)):
            if a_list[i].getName() == selected_animal:
                print(a_list[i])
                return i

        return -1

    def showAnimalCount(self):
        return f"Колличество животных: {self.__count}"

    def addAnimal(self):
        a = self.__model.addAnimalInModel(Animal(input("Введите имя: "), input(
            "Введите день рождения: "), input("Введите известные живоному команды: ")))

        print(f"Новое животное:\n{a}\n")
        print(self.__model.getAnimals_list())
        self.__count.add()

    def changeAnimalType(self, selected_animal):
        a_list = self.__model.getAnimals_list()
        if (self.__pickAnimal(selected_animal) != -1):
            i = self.__pickAnimal(selected_animal)
            user_input = input(
                "В какой класс вы хотите опеределить животное:\n1 - кошка\n2 - собака\n3 - хомяк\n4 - осел\n5 - лошадь\n6 - верлюд\n0 - для выхода в меню\n")

            if user_input == "1":
                a_list[i] = Cat(
                    a_list[i].getName(), a_list[i].getBirthday(), a_list[i].getCommands())
            elif user_input == "2":
                a_list[i] = Dog(
                    a_list[i].getName(), a_list[i].getBirthday(), a_list[i].getCommands())
            elif user_input == "3":
                a_list[i] = Hamster(
                    a_list[i].getName(), a_list[i].getBirthday(), a_list[i].getCommands())
            elif user_input == "4":
                a_list[i] = Donkey(
                    a_list[i].getName(), a_list[i].getBirthday(), a_list[i].getCommands())
            elif user_input == "5":
                a_list[i] = Horse(
                    a_list[i].getName(), a_list[i].getBirthday(), a_list[i].getCommands())
            elif user_input == "6":
                a_list[i] = Camel(
                    a_list[i].getName(), a_list[i].getBirthday(), a_list[i].getCommands())
            else:
                input(
                    "Такого класса нет!")

        else:
            input(
                "Такого животного нет!")

    def showAnimalCommands(self, selected_animal):
        a_list = self.__model.getAnimals_list()
        if (self.__pickAnimal(selected_animal) != -1):
            i = self.__pickAnimal(selected_animal)
            print(
                f"{a_list[i].getName()} знает команды: {a_list[i].getCommands()}")
        input(
            "Такого животного нет!")

    def addAnimalCommands(self, selected_animal):
        a_list = self.__model.getAnimals_list()
        if (self.__pickAnimal(selected_animal) != -1):
            i = self.__pickAnimal(selected_animal)
            user_input = input("Введите новую команду: ")
            a_list[i].setCommands(
                f"{a_list[i].getCommands()}  {user_input}")
            print(
                f"{a_list[i].getName()} знает команды: {a_list[i].getCommands()}")
        else:
            input(
                "Такого животного нет!")

    def getCountAnimals(self):
        return self.__count
