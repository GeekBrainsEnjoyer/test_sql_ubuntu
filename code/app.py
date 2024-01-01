
from animals.animalClasses import *
from mvp.presenter import Presenter


class App():
    def __init__(self, presenter=Presenter()) -> None:

        self.presenter = presenter

    def start(self):

        user_input = ""
        while user_input != "0":
            self.presenter.showAnimals()

            self.presenter.showAnimalCount()

            user_input = input(
                "\n1 - Завести новое животное\n2 - определять животное в правильный класс\n3 - увидеть список команд, которое выполняет животное\n4 - обучить животное новым командам\n0 - выход\n")

            if user_input == "1":
                self.presenter.addAnimal()

            elif user_input == "2":
                u_i = input("Введите имя животного: ")
                self.presenter.changeAnimalType(u_i)

            elif user_input == "3":
                u_i = input("Введите имя животного: ")
                self.presenter.showAnimalCommands(u_i)

            elif user_input == "4":
                u_i = input("Введите имя животного: ")
                self.presenter.addAnimalCommands(u_i)
