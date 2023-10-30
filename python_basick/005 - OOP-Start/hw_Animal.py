


class Human:
    def __init__(self):
        self.heals = 100
    def is_dangerous(self, animal):
        if animal.lower() == 'ядовитые' or animal == 'хищники':
            print(f' Carefully DANGEROUS ANIMAL !!!')

class Animal:

    def __init__(self, type_of_animal):
        self.type_of_animal = type_of_animal

man = Human()
lion = Animal('хищники')
cow = Animal('травоядные')
snake = Animal('ядовитые')
man.is_dangerous(lion.type_of_animal)
man.is_dangerous(cow.type_of_animal)
man.is_dangerous(snake.type_of_animal)





