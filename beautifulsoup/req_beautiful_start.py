

import requests
from bs4 import BeautifulSoup as bs

response = requests.get('https://books.toscrape.com/')

soup = bs(response.content, "html.parser")
section = soup.select("section")
books_block = section[0].select_one('ol[class=row]')
books = books_block.select('li')
# print(len(books))
# print(books)
books_data = []
for book in books:
    image = book.find('div', attrs={"class": "image_container"}).find("img")['src']
    print(image)





