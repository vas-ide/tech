from random import randint

# __________01__________
def random_error():
    dice = randint(1, 3)
    try:
        if dice == 1:
            raise ValueError
    except ValueError as v:
            print(f'ValueError')

    try:
        if dice == 2:
            raise TypeError
    except TypeError as t:
            print(f'TypeError')

    try:
        if dice == 3:
            raise RuntimeError
    except RuntimeError as r:
            print(f'RuntimeError')

random_error()

# __________02__________
def sort_list(lst):
    try:
        lst.sort()
        print(lst)
    except TypeError as v:
        print(f'ValueError')

sort_list([1, 21, 3, 45, 15, 7, 93])
sort_list([1, 21, 3, 45, 15, 7, 93, 'sys'])

# __________03__________
def dict_upg(dict_upg):
    print(f'Normal --- {dict_upg}')
    try:
        dict(dict_upg)
        new_dict = {}
        for key, value in dict_upg.items():
            new_dict[key] = str(value)
        print(f'Upg    --- {new_dict}')
    except TypeError as t:
        print(t)

list_upd = [1, 11, 111, 1111, 11111]
dict_upd_two = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}
dict_upg(list_upd)
dict_upg(dict_upd_two)
# __________04__________
def listed_upg(list_upg):
    print(f'Normal --- {list_upg}')
    try:
        type(list_upg) == list
        multiple_list = 1
        for i in list_upg:
            multiple_list *= i
        print(f'SUM --- {multiple_list}')
    except TypeError as t:
        print(t)

list_25 = [25, 125, -25, -100, 525]
listed_upg(list_25)
listed_upg('sys')
# __________05__________--- TEST
dict_upd_two = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}
new_dict = {}
for key, value in dict_upd_two.items():
    new_dict[key] = str(value)
print(new_dict)




