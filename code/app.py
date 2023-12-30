

from model.model import Model

from classes.animalClasses import Animal


class App():
    def __init__(self) -> None:
        self.model = Model()

    def start(self):
        self.model.addAnimal(Animal("qwe", "qwe", "qwe"))
        print(self.model.getAnimal_list())
        print("agagag")
