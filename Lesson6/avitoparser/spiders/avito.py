# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import HtmlResponse
from scrapy.loader import ItemLoader

from avitoparser.items import AvitoparserItem


class AvitoSpider(scrapy.Spider):
    name = 'avito'
    allowed_domains = ['avito.ru']
    start_urls = ['https://www.avito.ru/rossiya/kvartiry']

    def __init__(self, section):
        super(AvitoSpider, self).__init__()
        self.start_urls = [f'https://www.avito.ru/rossiya/{section}']

    def parse(self, response: HtmlResponse):
        links = response.css('a.snippet-link::attr(href)').extract()
        for link in links:
            yield response.follow(link, callback=self.parse_ads)

    def parse_ads(self, response: HtmlResponse):
        loader = ItemLoader(item=AvitoparserItem(), response=response)
        loader.add_css('photos', '.gallery-img-frame.js-gallery-img-frame::attr("data-url")')
        loader.add_css('name', 'span.title-info-title-text::text')
        loader.add_css('params', 'li.item-params-list-item')
        yield loader.load_item()
