import json
import requests
from lxml import html

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

        root = html.fromstring(response.text)
        news_container = root.xpath("/*[contains(@class, 'news news_y-xs')]")
        main_news_item = news_container.xpath("/*[contains(@class, 'news-item_main)")
        pass

