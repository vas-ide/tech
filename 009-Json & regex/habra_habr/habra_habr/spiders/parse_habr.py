import scrapy


class ParseHabrSpider(scrapy.Spider):
    name = "parse_habr"
    allowed_domains = ["habr.com"]
    start_urls = ["https://habr.com/ru/articles"]

    def parse(self, response):
        advertisements = response.xpath(".//div[class='tm-articles-list'/article")
        for advertisement in advertisements:
            yield {
                'title': advertisement.xpath(".//h2/a/span").get(),
                'text': advertisements.xpath(".//div[@class='article-formatted-body article-formatted-body article-formatted-body_version-2']/text()").get()
            }

