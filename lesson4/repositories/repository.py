import unicodedata
from datetime import datetime

import requests
from lxml import html


class Repository:
    __base_url: str = ''
    __source: str = ''
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

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, value: str):
        self.__source = value

    def collect_data(self):
        pass

    def get_data(self):
        response = requests.get(self.base_url, headers=self.__headers)
        if not response.ok:
            return None

        root = html.fromstring(unicodedata.normalize("NFKD", response.text))
        return root

    def prepare_data(self, item):
        pass

    def _get_news_date(self, link):
        response = requests.get(link)
        if not response.ok:
            return

        root = html.fromstring(unicodedata.normalize("NFKD", response.text))
        news_item_create_date = root.xpath("//*[contains(@class, 'js-ago')]/@datetime")
        return news_item_create_date[0] if len(news_item_create_date) > 0 else f"{datetime.today()}"



