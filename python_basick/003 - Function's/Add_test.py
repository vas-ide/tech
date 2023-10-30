import random

random_list = list(range(1, 16))
print(random_list)
random.shuffle(random_list)
print(random_list)
random_number = random.randint(0, 100)
print(random_number)


random_field = list(range(1, 16))
print(random_field)
random_field[-1] = 'random'
print(random_field)
random.shuffle(random_field)
print(random_field)

print(random_field[0: 0+4])
print(random_field[4: 4+4])
print(random_field[8: 8+4])
print(random_field[12: 12+4])
print('\n')

for i in range(0, 16, 4):
    print(random_field[i: i+4])
print('\n')

lst = [0, 3, 6, 9]
print(lst)
lst[0], lst[3] = lst[3], lst[0]
print(lst)
lst[1], lst[2] = lst[2], lst[1]
print(lst)
