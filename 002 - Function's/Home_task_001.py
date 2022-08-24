
# ----------01----------
numbers_list = [25, 33, 1 , 11, 255, 55, 11, 2, 5, 121]
new_numbers_list = numbers_list.sort()
print(numbers_list)
# ----------02----------
new_dict = {1: '1', 11: '1-1', 111: '111', 1111: '11-11', 11111: '11111', 111111: '111-111'}
for key, value in new_dict.items():
    print(key, value)
# ----------03----------
new_tuple = (12.5, 23.8, 78.5, 5.7, 1.9586, 255.9, 14.6, 5.5, 36.6, 152.5)
print(max(new_tuple))
print(min(new_tuple))
# ----------04----------
city_list = ['Eartsh', 'Russia', 'Moscow']
city_string = ''
for i in city_list:
    if i == city_list[-1]:
        city_string += i
    else:
        city_string += i
        city_string += ' -> '
print(city_string)
# ----------05----------
working_string = '/bin:/usr/bin:/usr/local/bin'
string = working_string.split(':')
print(string)
# ----------06----------
for i in range(100):
    if i % 7 == 0:
        print(f'Numbers {i} divide on 7!')
    else:
        print(f'Numbers {i} not divide on 7!')
# ----------07----------
for row in range(5, 9):
    for column in range(2, 5):
        # if ((column * row) < 10):
        #     print(" ", end="")
        print(column * row, end=" ")
    print()
# ----------08----------
object_list = ['Alex', 'Leonid', 'Ksenia', 'Tatiana', 'Andrei', 'Viktoria', 'Andrei', 'Kian', 'Olga',
               'Ludmila', 'Luiza']
for index, name in enumerate(object_list):
    print(f'Name {name} number in list -{index}!')
# ----------09----------
# ----------10----------
# ----------11----------













