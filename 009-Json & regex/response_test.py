


import requests

def get_habrahabr():
    url = "http://habrahabr.ru"
    response = requests.get(url=url)
    print(
        response.status_code,
        response.headers,
        # response.content,
        response.text
    )
# def find_pet_by_tag(tag):
#     params = {"tags": tag}
#     headers = {
#         "Accept" "application/xml",
#         # "Accept" "application/json"
#     }
#     url = "http://petstore.swagger.io/v2/pet/findByTags"
#     response = requests.get(url=url, params=params, headers=headers)
#     print(
#         response.status_code,
#         response.headers,
#         # response.content,
#         response.text
#     )
# # find_pet_by_tag("cat")


def find_by_tag():
    pattern = r"href="
    params = {"tags": "link"}
    headers = {
        # "Accept" "application/xml",
        # "Accept" "application/json"
    }
    url = "http://habrahabr.ru"
    response = requests.get(url=url, params=params, headers=headers)
    print(
        response.status_code,
        response.headers,
        # response.content,
        response.text
    )
find_by_tag()




