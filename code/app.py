

from model.model import Model

from animals.animalClasses import Animal


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
                    user_input = input("Введите имя животного: ")
                    for i in range(len(a_list) - 1):
                        if a_list[i].name == user_input:
                            chosen_animal = a_list[i].name
                        else:
                            print(
                                "Такого животного нет. Введите имя еще раз или 0 для выхода.")

                    user_input = input(
                        "В какой класс вы хотите опеределить животное:\n1 - кошка\n2 - собака\n3 - хомяк\n4 - осел\n5 - лошадь\n6 - верлюд\n0 - для выхода в меню\n")
