from functools import reduce

# + При помощи map посчитать остаток от деление на 5 для чисел: [1, 4, 5, 30, 99]
# + При помощи map превратить все числа из массива [3, 4, 90, -2] в строки
# + При помощи filter убрать из массива ['some', 1, 'v', 40, '3a', str] все строки
# + При помощи reduce посчитать количество букв в словах: ['some', 'other', 'value'].

lst = [1, 4, 5, 30, 99]
result = map(lambda x: x % 5, lst)
print(list(result))


lst = [3, 4, 90, -2]
result = list(map(lambda x: str(x), lst))
print(result)


lst_f = ['some', 1, 'v', 40, '3a', str]
result = list(filter(lambda x: type(x) != str, lst_f))
print(list(result))


lst_r = ['some', 'other', 'value']
result = len(reduce(lambda x, y: x + y, lst_r))
print(result)