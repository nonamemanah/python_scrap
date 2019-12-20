import typing
import requests

from bs4 import BeautifulSoup as bs
from lesson2.entity.Salary import Salary
from lesson2.entity.Vacancy import Vacancy

class Repository:
    """
    Абстрактный класс репозиториев
    """
    __user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                   'Chrome/78.0.3904.108 Safari/537.36 '

    __payload_key = ''

    __item_class: str = ''
    __title_class: str = ''
    __link_class: str = ''
    __compensation_class: str = ''

    _base_url: str = ''

    def __init__(self, source: str):
        self.__source = source

    def get_data(self, name: str) -> typing.List[Vacancy]:
        """
        Получить данные
        """
        result = []
        payload = {self.payload_key: name}
        headers = {
            'user-agent': self.__user_agent}
        response = requests.get(self.base_url, params=payload, headers=headers)
        if not response.ok:
            return []

        parser = self.parser(response.text)

        items = parser.select(self.item_class)
        for item in items:
            vacancy_item_title = item.select(self.title_class)
            vacancy_link = item.select(self.link_class)
            vacancy__compensation = item.select(self.compensation_class)

            title = vacancy_item_title[0].text.strip()
            link = vacancy_link[0]['href']

            compensation = '' if len(vacancy__compensation) == 0 else vacancy__compensation[0].text.strip()
            result.append(Vacancy(title, Salary(compensation), link, self.__source))

        return result

    @property
    def base_url(self):
        """
        Базовый URL
        """
        return self._base_url

    @base_url.setter
    def base_url(self, value):
        """
        Базовый URL
        """
        self._base_url = value

    @property
    def item_class(self):
        return self.__item_class

    @item_class.setter
    def item_class(self, value):
        self.__item_class = value

    @property
    def title_class(self):
        return self.__title_class

    @title_class.setter
    def title_class(self, value):
        self.__title_class = value

    @property
    def link_class(self):
        return self.__link_class

    @link_class.setter
    def link_class(self, value):
        self.__link_class = value

    @property
    def compensation_class(self):
        return self.__compensation_class

    @compensation_class.setter
    def compensation_class(self, value):
        self.__compensation_class = value

    @property
    def payload_key(self):
        return self.__payload_key

    @payload_key.setter
    def compensation_class(self, value):
        self.__payload_key = value

    def parser(self, html: str):
        return bs(html, 'lxml')
