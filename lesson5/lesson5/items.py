# -*- coding: utf-8 -*-

import scrapy


class JobItem(scrapy.Item):
    name = scrapy.Field()
    salary = scrapy.Field()
    link = scrapy.Field()
    source = scrapy.Field()
