# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from pymongo import MongoClient
from scrapy.pipelines.images import ImagesPipeline


class AvitoparserPhotosPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        if item['photos']:
            for photo_url in item['photos']:
                try:
                    yield scrapy.Request(photo_url)
                except Exception as e:
                    print(e)

    def item_completed(self, results, item, info):
        if results:
            item['photos'] = [itm[1] for itm in results if [itm[0]]]
        return item

class AvitoDbPipline(object):
    def __init__(self):
        client = MongoClient('localhost', 27017)
        self.mongo_client = client.avito

    def process_item(self, item, spider):
        try:
            collection = self.mongo_client[spider.name]
            collection.insert_one(item)
        except Exception as e:
            print(e)
        return item