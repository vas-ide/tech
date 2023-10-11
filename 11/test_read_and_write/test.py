import sys

import random

import os

cwd = os.getcwd()
files = os.listdir(cwd)
print(cwd, files)


# for i in range(100):
#     with open("test_info.txt", "a", encoding="utf8") as info:
#         info_str = f"Id - {random.randint(1, 1000000000)} is empty"
#         print(info_str)
#         info.write(f"Numbers = {info_str}\n")
#


def write_to_file(file, information, mode="w", ):
    with open(file, mode=mode, encoding="utf-8") as info:
        info.write(f"{information}\n")


# for i in range(100):
#     info_str = f"Id - {random.randint(1, 5000)} is empty"
#     write_to_file("test_info.txt", f"{info_str}", mode="a")


def read_to_file(file, mode="r"):
    with open(file=file, mode=mode, encoding='utf-8') as info:
        # for i in info:
        #     print(i)
        print(info.read())


read_to_file("/home/vas-ide/Documents/Python/tech/11/test_read_and_write/test_info.txt")
