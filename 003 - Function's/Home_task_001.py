
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
list_for_example = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
human_flag(list_for_example, True)
human_flag(list_for_example, False)
# __________05__________
# __________06__________
# __________07_________
# __________08__________
# __________09__________
# __________10__________
# __________11__________
