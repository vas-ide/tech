

import requests
from bs4 import BeautifulSoup as bs

class ParseBook:
    def __init__(self, html_parse):
        self.marker = True
        self.books_data = []
        self.start_page = html_parse

    def run(self):
        while self.marker == True:

            response = requests.get(self.start_page)
            if response.status_code == 200:
                soup = bs(response.content, "html.parser")
                section = soup.select("section")
                books_block = section[0].select_one('ol[class=row]')
                books = books_block.select('li')
                for book in books:
                    image = book.find('div', attrs={"class": "image_container"}).find("img")['src']
                    image_src_full = f"https://books.toscrape.com/{image}"
                    title = book.find('h3').find("a")['title']
                    price = book.find('div', attrs={"class": "product_price"}).find("p").text
                    # print(f"{image_src_full:<86}{title:<205}{price}")
                    books_dict = {"image": image,
                                  "title": title,
                                  "price": price}
                    self.books_data.append(books_dict)


                try:
                    next_page = soup.find('li', attrs={"class": "next"}).find("a")['href']
                    next_page = f"https://books.toscrape.com/catalogue/{next_page}"
                    self.start_page = next_page
                except:
                    self.marker = False
                    # print(len(self.books_data))

books = ParseBook('https://books.toscrape.com/catalogue/page-1.html')
books.run()
print(books.books_data)