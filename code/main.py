from app import App
from animals.animalClasses import*

from model.model import Model

saved_list = [Cat("qwe1", "qwe", "qwe"),
              Dog("qwe2", "qwe", "qwe"),
              Horse("qwe3", "qwe", "qwe"),
              Cat("qwe4", "qwe", "qwe")]

a = App(Model(saved_list))

# a = App()
a.start()
