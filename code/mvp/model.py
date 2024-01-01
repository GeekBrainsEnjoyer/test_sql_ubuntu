from animals.animalClasses import Animal
from animals.animalCount import AnimalCount


class Model:
    def __init__(self, animal_list=[]) -> None:
        self.animal_list = animal_list
        self.count = AnimalCount()
        self.count.setCount(len(animal_list))

    def addAnimalInModel(self, animal: Animal):
        self.animal_list.append(animal)
        self.count.add()
        return animal

    def deltAnimal(self, animalName):
        for i in range(len(self.animal_list)):
            if self.animal_list[i].name == animalName:
                del self.animal_list[i]
        self.count.delt()

    def getAnimals_list(self):
        return self.animal_list

    def __str__(self) -> str:
        str = ""
        for i in range(len(self.animal_list)):
            str += f"{self.animal_list[i]}\n\n"
        return str
