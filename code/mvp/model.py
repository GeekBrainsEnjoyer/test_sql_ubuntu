from animals.animalClasses import Animal
from animals.animalCount import AnimalCount


class Model:
    def __init__(self, animal_list=[]) -> None:
        self.__animals_list = animal_list
        

    def addAnimalInModel(self, animal: Animal):
        self.__animals_list.append(animal)
        return animal

    def getAnimals_list(self):
        return self.__animals_list
    
    
    def __str__(self) -> str:
        str = ""
        for i in range(len(self.__animals_list)):
            str += f"{self.__animals_list[i]}\n"
        return str
