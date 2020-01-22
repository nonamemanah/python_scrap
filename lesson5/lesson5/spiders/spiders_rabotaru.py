# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import HtmlResponse

from lesson5.lesson5.items import JobItem


class RabotaruSpider(scrapy.Spider):
    name = 'spiders.superjob'
    allowed_domains = ['https://www.rabota.ru/vacancy/?query=python&sort=relevance']
    start_urls = ['https://www.rabota.ru/']

    def parse(self, response: HtmlResponse):
        links = response.css('a[itemprop="title"]::attr(href)').extract();
        for link in links:
            yield response.follow(link, callback=self.parse_vacancy)

    def parse_vacancy(self, response: HtmlResponse):
        name = response.css('h1[itemprop="title"]::text').extract_first()
        salary = response.css('h3[baseSalary="baseSalary"]::text').extract()
        link = response.request.url
        source = 'rabotaru'
        yield JobItem(name=name, salary=salary, link=link, source=source)
        pass
