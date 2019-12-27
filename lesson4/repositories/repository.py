import json
import requests
import unicodedata
from lxml import html
from pprint import pprint

class Repository:
    __base_url: str = ''
    __user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                   'Chrome/78.0.3904.108 Safari/537.36'
    __headers = {'user-agent': __user_agent}

    def __init__(self):
        pass

    @property
    def base_url(self):
        return self.__base_url

    @base_url.setter
    def base_url(self, value):
        self.__base_url = value

    def get_data(self):
        response = requests.get(self.base_url, headers=self.__headers)
        if not response.ok:
            return []

        root = html.fromstring(unicodedata.normalize("NFKD", response.text))
        news_container = root.xpath("//*[@id='news']/div[contains(@class, 'news-item')]")
        for item in news_container[:-3]:
            self.__prepare_data(item)

    def __prepare_data(self, item):
        link = item.xpath('.//a')[0]
        link_text = link.xpath('.//text()')[0]
        link_href = item.xpath('.//a/@href')[0]
        pprint(link_text)
        pprint(link_href)
        self.__get_datail_news(link_href)

    def __get_datail_news(self, link):
        response = requests.get(link)
        if not response.ok:
            return

        root = html.fromstring(unicodedata.normalize("NFKD", response.text))
        news_item_create_date = root.xpath("//*[contains(@class, 'js-ago')]/@datetime")
        print(news_item_create_date)



