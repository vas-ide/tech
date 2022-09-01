
# __________01__________
list_random_len = [1, 2, 3, 4, 5, 'one', 'two', 'three', 'four', 'five']
def index_unpredictable(list, index):
    try:
        print(f'Index={index} answer = {list[index]}')
    except IndexError as i:
        print(f'IndexError --- {i}')
index_unpredictable(list_random_len, 5)
index_unpredictable(list_random_len, 10)
index_unpredictable(list_random_len, 1)
# __________02__________
def calc(num1, num2):
    if num1 > 0 and num2 > 0:
        print(num1 + num2)
        return num1 + num2
    elif num1 < 0 and num2 < 0:
        print(num1 - num2)
        return num1 - num2
    elif num1 > 0 and num2 < 0 or num1 < 0 and num2 > 0:
        print(0)
        return 0
calc(1, 10)
calc(-1, -10)
calc(1, -10)
# __________03__________
def max_num(num1, num2, num3):
    work_list = []
    work_list.append(num1)
    work_list.append(num2)
    work_list.append(num3)
    max1 = max(work_list)
    work_list.remove(max1)
    max2 = max(work_list)
    print(f'First max number = {max1}, Second max number = {max2}')
max_num(10, 15, 20)
# __________04__________
def human_flag(lst, flag=True):
    new_lst = []
    if flag == True:
        for i in lst:
            if i % 2 != 0:
                new_lst.append(i)
        print(f'True {new_lst}')
        return new_lst

    if flag == False:
        for i in lst:
            if i % 2 == 0:
                new_lst.append(i)
        print(f'False {new_lst}')
        return False
string_for_example = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
human_flag(string_for_example, True)
human_flag(string_for_example, False)
# __________05__________
def max_and_min_numbers(*args):
    min_and_max_lst = []
    for i in args:
        if type(i) == int or type(i) == float:
            min_and_max_lst.append(i)
    print(max(min_and_max_lst))
    print(min(min_and_max_lst))
max_and_min_numbers(1, 0.2, 45, 8, 86, 5)
max_and_min_numbers(1, 0.2, 45, 8, 86, 5, 'sus')
# __________06__________
def human_flag(string, flag=True):
    new_string = ''
    if flag == True:
        for i in string:
            new_string += i.upper()
        print(new_string)
        return new_string

    if flag == False:
        for i in string:
            new_string += i.lower()
        print(new_string)
        return False
string_for_example = 'Hello my friend. My name is Alex. I am 35 e.o.'
human_flag(string_for_example, True)
human_flag(string_for_example, False)
# __________07_________
def sum_string(*args, glue=':'):
    new_str_sum = ''
    for i in args:
        if type(i) == str and len(i) > 3:
            if len(new_str_sum) > 3:
                new_str_sum += glue
                new_str_sum += i
            else:
                new_str_sum += i
    print(new_str_sum)
    # return new_str_sum
sum_string('12345', '12', '6789', '0', '9876', '56', '54321')
# __________08__________
# __________09__________
# __________10__________
# __________11__________
