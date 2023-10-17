

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
    image_src_full = f"https://books.toscrape.com/{image}"
    title = book.find('h3').find("a")['title']
    price = book.find('div', attrs={"class": "product_price"}).find("p").text
    # print(f"{image_src_full:<90}{title:<100}{price}")
    books_dict = {"image": image,
                  "title": title,
                  "price": price}
    books_data.append(books_dict)

[print(i) for i in books_data]





