from app import App
from animals.animalClasses import *

from model.model import Model

saved_list = [Cat("cat", "qwe", "qwe"),
              Animal("a1", "qwe", "qwe"),
              Animal("a2", "qwe", "qwe"),
              Dog("dog", "qwe", "qwe"),
              Horse("horse", "qwe", "qwe"),
              Animal("a3", "qwe", "qwe")]

a = App(Model(saved_list))

# a = App()
a.start()
