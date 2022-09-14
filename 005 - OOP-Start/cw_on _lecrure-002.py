



class Numbers:
    def __init__(self):
        self.list_numbers = []

    def add_numbers(self, *args):
        while True:
            self.list_numbers = []
            args = input(f'Input Number\'s or Number ==> maximum four number\'s ').split()
            for i in args:
                self.list_numbers.append(int(i))
            if len(self.list_numbers) <= 4:
                break

    def construction(self):
        if len(self.list_numbers) == 1:
            s = self.list_numbers[0] * self.list_numbers[0]
            p = self.list_numbers[0] + self.list_numbers[0] + self.list_numbers[0] + self.list_numbers[0]
            print(f'Square S = {s} P = {p}')
        elif len(self.list_numbers) == 2:
            s = self.list_numbers[0] * self.list_numbers[1]
            p = self.list_numbers[0] + self.list_numbers[1] + self.list_numbers[0] + self.list_numbers[1]
            print(f'Rectangle S = {s} P = {p}')
        elif len(self.list_numbers) == 3:
            p = self.list_numbers[0] + self.list_numbers[1] + self.list_numbers[2]
            print(f'Triangle P = {p}')
        elif len(self.list_numbers) == 4:
            p =   p = self.list_numbers[0] + self.list_numbers[1] + self.list_numbers[2] + self.list_numbers[3]
            print(f'Polygon P = {p}')

numbers = Numbers()
numbers.add_numbers()
numbers.construction()



