

class Basket:
    def __init__(self):
        self.total_capacity = 100

    def add_in_basket(self, add):
        if self.total_capacity < add:
            print(f'Нет места в корзине всего осталось {self.total_capacity} kg')
        else:
            self.total_capacity -= add
            print(f'Добавлено {add} kg осталось {self.total_capacity} kg')

class Package:
    def __init__(self):
        self.total_capacity = 10

    def add_in_package(self, add):
        if self.total_capacity < add:
            print(f'Нет места в пакете всего осталось {self.total_capacity} kg')
        else:
            self.total_capacity -= add
            print(f'Добавлено {add} kg осталось {self.total_capacity} kg')

class Potato: # Картофель
    def __init__(self):
        self.total_weight = 15

class Carrot: # Морковь
    def __init__(self):
        self.total_weight = 5

class Onion: # Лук
    def __init__(self):
        self.total_weight = 5

class Garlic: # Чеснок
    def __init__(self):
        self.total_weight = 2.5


basket = Basket()
package = Package()
potato = Potato()
carrot = Carrot()
onion = Onion()
garlic = Garlic()

package.add_in_package(potato.total_weight)
package.add_in_package(carrot.total_weight)
package.add_in_package(garlic.total_weight)
package.add_in_package(onion.total_weight)
basket.add_in_basket(potato.total_weight)
basket.add_in_basket(onion.total_weight)












