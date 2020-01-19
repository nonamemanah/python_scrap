import re

from lesson4.entity.news import News
from lesson4.repositories.db_repository import DbRepository
from lesson4.repositories.repository import Repository


class MailRepository(Repository):

    def __init__(self):
        self.base_url = 'https://mail.ru'
        self.__source = 'mail.ru'
        self.__db = DbRepository()

    def collect_data(self):
        result = []
        root = super().get_data()
        news_container = root.xpath("//*[@id='news']/div[contains(@class, 'news-item')]")
        for item in news_container[:-3]:
            news_item = self.prepare_data(item)
            result.append(news_item)
        return result

    def prepare_data(self, item):
        link = item.xpath('.//a')[0]
        link_text = link.xpath('.//text()')[0]
        link_href = item.xpath('.//a/@href')[0]
        if len(re.findall("^(http|https)://", link_href)) == 0:
            link_href = f"{self.base_url}{link_href}"
        news_date = self._get_news_date(link_href)
        return News(self.__source, link_text, link_href, news_date)

