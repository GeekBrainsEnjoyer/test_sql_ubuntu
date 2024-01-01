from app import App
from animals.animalClasses import *

from mvp.model import Model
from mvp.presenter import Presenter

saved_list = [Cat("cat", "qwe", "qwe"),
              Animal("a1", "qwe", "qwe"),
              Animal("a2", "qwe", "qwe"),
              Dog("dog", "qwe", "qwe"),
              Horse("horse", "qwe", "qwe"),
              Animal("a3", "qwe", "qwe")]

a = App(Presenter(Model(saved_list)))

# a = App()
a.start()
