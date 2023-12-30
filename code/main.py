from app import App
from animals.animalClasses import *

from model.model import Model

saved_list = [Cat("cat", "qwe", "qwe"),
              Animal("qwe", "qwe", "qwe"),
              Animal("qwe", "qwe", "qwe"),
              Dog("dog", "qwe", "qwe"),
              Horse("horse", "qwe", "qwe"),
              Animal("qwe", "qwe", "qwe")]

a = App(Model(saved_list))

# a = App()
a.start()
