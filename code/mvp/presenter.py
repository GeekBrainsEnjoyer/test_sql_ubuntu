from animals.animalClasses import *
from mvp.model import *


class Presenter:
    def __init__(self, model=Model()) -> None:
        self.model = model

    def showAnimals(self):
        if len(self.model.animal_list) == 0:
            print("Животных нет!")
        else:
            print(f"Список животных:\n{self.model}")

    def __pickAnimal(self, selected_animal: str):
        a_list = self.model.getAnimals_list()
        for i in range(len(a_list)):
            if a_list[i].getName() == selected_animal:
                print(a_list[i])
                return i

        return -1

    def showAnimalCount(self):
        return f"Колличество животных: {self.model.count.getCount()}"

    def addAnimal(self):
        a = self.model.addAnimalInModel(Animal(input("Введите имя: "), input(
            "Введите день рождения: "), input("Введите известные живоному команды: ")))

        print(f"Новое животное:\n{a}\n")
        return True

    def changeAnimalType(self, selected_animal):
        a_list = self.model.getAnimals_list()
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
                print(
                    "Такого класса нет. Введите имя еще раз или 0 для выхода.")

        else:
            print(
                "Такого животного нет. Введите имя еще раз или 0 для выхода.")

    def showAnimalCommands(self, selected_animal):
        a_list = self.model.getAnimals_list()
        if (self.__pickAnimal(selected_animal) != -1):
            i = self.__pickAnimal(selected_animal)
            print(
                f"{a_list[i].getName()} знает команды: {a_list[i].getCommands()}")
        else:
            print(
                "Такого животного нет. Введите имя еще раз или 0 для выхода.")

    def addAnimalCommands(self, selected_animal):
        a_list = self.model.getAnimals_list()
        if (self.__pickAnimal(selected_animal) != -1):
            i = self.__pickAnimal(selected_animal)
            user_input = input("Введите новую команду: ")
            a_list[i].setCommands(
                f"{a_list[i].getCommands()}  {user_input}")
            print(
                f"{a_list[i].getName()} знает команды: {a_list[i].getCommands()}")
        else:
            print(
                "Такого животного нет. Введите имя еще раз или 0 для выхода.")
