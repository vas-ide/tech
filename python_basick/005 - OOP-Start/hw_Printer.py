



class Printer:
    def __init__(self):
        self.list_for_printed = []
    def log(self, *args):
        self.list_for_printed = []
        args = input(f'Input information == >>>   ').split()
        for i in args:
            self.list_for_printed.append(i)
            print(i)

class FormattedPrinter(Printer):

    def log(self, *args):
        args = input(f'Input information == >>>   ').split()
        for i in args:
            star = '*'
            print(f'{star * 52}')
            print(f'{star * 5} {i:^40} {star * 5}') # 52 из за пробелов
            print(f'{star * 52}')





printer = FormattedPrinter()
printer.log()









