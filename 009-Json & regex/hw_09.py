import json
import sys

import os

import requests

cwd = os.getcwd()
files = os.listdir(cwd)
print(cwd, files)


# for i in range(100):
#     with open("test_info.txt", "a", encoding="utf8") as info:
#         info_str = f"Id - {random.randint(1, 1000000000)} is empty"
#         print(info_str)
#         info.write(f"Numbers = {info_str}\n")
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


# read_to_file("/home/vas-ide/Documents/Python/tech/009/test_read_and_write/test_info.txt")


#  Реализовать следующую логику: получать при помощи requests данные сервиса https://jsonplaceholder.typicode.com/
# (сущность можно выбрать любую, например https://jsonplaceholder.typicode.com/comments),
# выводить в консоль все пары заголовки, сохранять полученный json в файл на диск

# response = requests.get("https://jsonplaceholder.typicode.com/")
# response_com = requests.get("https://jsonplaceholder.typicode.com/comments")
# response_com_json = json.loads(response_com.text)
# for str_in_json in response_com_json:
#     write_to_file("/home/vas-ide/Documents/Python/tech/009/test_read_and_write/json_comments.txt",
#                   f"___{str_in_json['name']}___\n{str_in_json['body']}\n", "a")

# response_reddit = requests.get("https;//reddit.com/r/python/")
# print(response_reddit.text)


response_habr = requests.get("https://habrahabr.ru/")
print(response_habr.text)
print(response_habr.cookies)
print(response_habr.info())









