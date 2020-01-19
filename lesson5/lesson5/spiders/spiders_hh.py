# -*- coding: utf-8 -*-
import pprint

import scrapy
from scrapy.http import HtmlResponse
from bs4 import BeautifulSoup as bs

from lesson5.lesson5.items import HeadHunterItem


class SpidersHhSpider(scrapy.Spider):
    name = 'spiders.hh'
    allowed_domains = ['hh.ru']
    start_urls = ['https://hh.ru/search/vacancy?area=1&st=searchVacancy&text=python']

    def parse(self, response: HtmlResponse):
        next_button = response.css('.bloko-button.HH-Pager-Controls-Next.HH-Pager-Control::attr(href)').get()
        yield response.follow(next_button, callback=self.parse)

        items = response.css('.vacancy-serp-item').extract()
        for item in items:
            yield self.parse_vacancy(item)

    def parse_vacancy(self, vacancy_item: str):
        parser = self.parser(vacancy_item)
        item = HeadHunterItem()
        item.fields['name'] = parser.select('.bloko-link.HH-LinkModifier')[0].text.strip()
        item.fields['salary'] = parser.select('.vacancy-serp-item__compensation')[0].text.strip()
        item.fields['link'] = parser.select('.bloko-link.HH-LinkModifier')[0]['href']
        item.fields['source'] = 'hh.ru'
        return item

    def parser(self, html: str):
        return bs(html, 'lxml')
