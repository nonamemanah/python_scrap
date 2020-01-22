# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import HtmlResponse

from lesson5.lesson5.items import JobItem


class HhSpider(scrapy.Spider):
    name = 'spiders.hh'
    allowed_domains = ['hh.ru']
    start_urls = ['https://hh.ru/search/vacancy?area=1&st=searchVacancy&text=python']

    def parse(self, response: HtmlResponse):
        next_button = response.css('.bloko-button.HH-Pager-Controls-Next.HH-Pager-Control::attr(href)').get()
        yield response.follow(next_button, callback=self.parse)

        items_href = response.css('a[data-qa="vacancy-serp__vacancy-title"]::attr(href)').extract()
        for item in items_href:
            yield response.follow(item, callback=self.parse_vacancy)

    def parse_vacancy(self, response: HtmlResponse):
        name = response.css('h1[data-qa="vacancy-title"]>span::text').extract_first()
        salary = ''.join(response.css('p.vacancy-salary::text').extract())
        link = response.request.url
        source = 'hh.ru'
        yield JobItem(name=name, salary=salary, link=link, source=source)
