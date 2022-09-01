




number = int(input('Input a number - '))
if number % 2 == 0:
    try:
        number % 2 == 0
        int('number')
    except ValueError:
        print('ValueError')
        print(f'Int from string')
        print(f'Ошибка ValueError в Python возникает, когда функция получает аргумент правильного типа, '
              f'но несоответствующее значение.')
elif number < 0:
    try:
        number + 'number'
    except TypeError:
        print('TypeError')
        print(('Sun int and string'))
        print(f'Ошибки TypeError возникают, когда функция или операция применяется к объекту неправильного типа '
              f'и они не совместимы.')
elif number > 10:
    try:
        str(number)[10]
    except IndexError:
        print('IndexError')
        print(f'More over index')
        print('IndexError. Исключение, возникающее при обращении к элементу по индексу, находящемуся вне диапазона. '
              'Поднимается при попытках обратиться к элементу последовательности, используя индекс, '
              'выходящий за пределы поддерживаемого последовательностью диапазона. ')


























