
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
# __________04__________
# __________05__________
# __________06__________
# __________07_________
# __________08__________
# __________09__________
# __________10__________
# __________11__________
