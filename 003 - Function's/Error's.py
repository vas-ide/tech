




number = int(input('Input a number - '))
if number % 2 == 0:
    try:
        number % 2 == 0
        int('number')
    except ValueError as v:
        print('ValueError')
        print(f'Int from string')
        print(v)
        print(f'Ошибка ValueError в Python возникает, когда функция получает аргумент правильного типа, '
              f'но несоответствующее значение.')
elif number < 0:
    try:
        number + 'number'
    except TypeError as t:
        print('TypeError')
        print(('Sun int and string'))
        print(t)
        print(f'Ошибки TypeError возникают, когда функция или операция применяется к объекту неправильного типа '
              f'и они не совместимы.')
elif number > 10:
    try:
        str(number)[10]
    except IndexError as i:
        print('IndexError')
        print(f'More over index')
        print(i)
        print('IndexError. Исключение, возникающее при обращении к элементу по индексу, находящемуся вне диапазона. '
              'Поднимается при попытках обратиться к элементу последовательности, используя индекс, '
              'выходящий за пределы поддерживаемого последовательностью диапазона. ')




# vvod = input('Введите любое число:')
# n = int(vvod)
# try:
#     if n < 0:
#         raise TypeError ('Число меньше нуля')
#     if n > 10:
#         raise IndexError ('Число больше десяти')
#     if n % 2 == 0:
#         raise ValueError ('Число четное')
# except TypeError :
#     print('Число меньше нуля')
# except IndexError :
#     print('Число больше десяти')
# except ValueError :
#     print('Число четное')





















