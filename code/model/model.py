from classes.animalClasses import Animal


class Model:
    def __init__(self, animal_list=[]) -> None:
        self.animal_list = animal_list

    def addAnimal(self, animal: Animal):
        self.animal_list.append(animal)
        print('ffdfd')
        
    def getAnimal_list(self):
        return self.animal_list
