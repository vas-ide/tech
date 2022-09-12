




class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.know_person_list = []

    def know_person(self, name):
        self.know_person_list.append(name)

    def check_knowing(self, name):
        if name in self.know_person_list:
            print(f'{self.name} know this person')
            return True, f'{self.name} know this person'
        else:
            print(f'{self.name} don\'t know this person')
            return False, f'{self.name} don\'t know this person'

im = Person('Alex', 35)
print(im.name, im.age)
im.know_person('Tatiana')
im.know_person('Ksy')
im.know_person('Leonid')
print(im.know_person_list)
im.check_knowing('Ksy')
im.check_knowing('Alex')













