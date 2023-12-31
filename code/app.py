

from model.model import Model

from animals.animalClasses import *


class App():
    def __init__(self, model=Model()) -> None:
        self.model = model

    def start(self):

        user_input = ""
        while user_input != "5":
            if len(self.model.animal_list) == 0:
                print("Животных нет!")
            else:
                print(f"Список животных:\n{self.model}")

            print(f"Колличество животных: {self.model.count.getCount()}")
            user_input = input(
                "\n1 - Завести новое животное\n2 - определять животное в правильный класс\n3 - увидеть список команд, которое выполняет животное\n4 - обучить животное новым командам\n5 - выход\n")

            if user_input == "1":
                a = self.model.addAnimal(Animal(input("Введите имя: "), input(
                    "Введите день рождения: "), input("Введите известные живоному команды: ")))
                print(f"Новое животное:\n{a}")

            elif user_input == "2":
                a_list = self.model.animal_list
                chosen_animal = ""
                print(self.model)
                while user_input != "0":
                    user_input = input(
                        "Введите имя животного или 0 для выхода в меню: ")
                    for i in range(len(a_list)):
                        if a_list[i].name == user_input:
                            chosen_animal = a_list[i].name
                            print(a_list[i])
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

                    if chosen_animal == "":
                        print(
                            "Такого животного нет. Введите имя еще раз или 0 для выхода.")

            elif user_input == "3":
                a_list = self.model.animal_list
                chosen_animal = ""
                while user_input != "0":
                    user_input = input(
                        "Введите имя животного или 0 для выхода в меню: ")
                    for i in range(len(a_list)):
                        if a_list[i].name == user_input:
                            chosen_animal = a_list[i].name
                            print(
                                f"{a_list[i].getName()} знает команды: {a_list[i].getCommands()}")

                    if chosen_animal == "":
                        print(
                            "Такого животного нет. Введите имя еще раз или 0 для выхода.")

            elif user_input == "4":
                a_list = self.model.animal_list
                chosen_animal = ""
                while user_input != "0":
                    user_input = input(
                        "Введите имя животного или 0 для выхода в меню: ")
                    for i in range(len(a_list)):
                        if a_list[i].name == user_input:
                            chosen_animal = a_list[i].name
                            user_input = input("Введите новую команду: ")
                            a_list[i].setCommands(
                                f"{a_list[i].getCommands()}  {user_input}")
                            print(
                                f"{a_list[i].getName()} знает команды: {a_list[i].getCommands()}")

                    if chosen_animal == "":
                        print(
                            "Такого животного нет. Введите имя еще раз или 0 для выхода.")
