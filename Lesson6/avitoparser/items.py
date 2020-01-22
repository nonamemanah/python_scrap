# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import TakeFirst, MapCompose

def clean_photo(value):
    return f'http:{value}' if value[:2] == '//' else value

class AvitoparserItem(scrapy.Item):
    _id = scrapy.Field()
    photos = scrapy.Field(input_processor=MapCompose(clean_photo))
    name = scrapy.Field(output_processor=TakeFirst())
    params = scrapy.Field()
