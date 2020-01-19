# -*- coding: utf-8 -*-

import scrapy


class HeadHunterItem(scrapy.Item):
    name = scrapy.Field()
    salary = scrapy.Field()
    link = scrapy.Field()
    source = scrapy.Field()
