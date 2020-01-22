# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient


class Lesson5Pipeline(object):
    def __init__(self):
        client = MongoClient('localhost', 27017)
        self.mongo_client = client.vacancies

    def process_item(self, item, spider):
        collection = self.mongo_client[spider.name]
        collection.insert(item)
        return item
