



# # _____01_____
# a = float(input('Rectangle side. - '))
# b = float(input('Rectangle side. - '))
# print('Square rectangle', a * b)
# # _____02_____
# a = float(input('First number. - '))
# b = float(input('Second number. - '))
# opr = input('Simple operation. -  ')
# if opr == '+':
#     print('Operation "+"', a + b)
# elif opr == '-':
#     print('Operation "-"', a - b)
# elif opr == '*':
#     print('Operation "*"', a * b)
# elif opr == '/':
#     print('Operation "-"', a / b)

# _____03_____
# num = int(input('Input number. - '))
# counter = 0
# while counter <= num:
#     counter += 1
#     count = 0
#     for i in range(10000):
#         if i == 0:
#             pass
#         elif counter % i == 0:
#             count += 1
#     if count == 2:
#         print(f'Simple number - {counter}')

# _____04_____
a = int(input('First number. - '))
b = int(input('Second number. - '))
max_num = a
min_num = b
if a < b:
    max_num = b
    min_num = a
while min_num <= max_num:
    min_num += 1
    if min_num % 5 == 0:
        print(f'{min_num}')





