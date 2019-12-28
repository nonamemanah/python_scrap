from lesson4.Models.news_item_view_model import NewsItemViewModel
from lesson4.entity.news import News
from lesson4.repositories.db_repository import DbRepository
from lesson4.repositories.mail_repository import MailRepository


class NewsService:
    __mail_repository: MailRepository
    __db_repository: DbRepository

    def __init__(self):
        self.__mail_repository = MailRepository()
        self.__db_repository = DbRepository()

    def sync_news(self):
        items = self.__mail_repository.get_data()
        session = self.__db_repository.create_session()
        session.add_all(items)
        session.commit()
        session.close()

    def get_news(self):
        result = []
        session = self.__db_repository.create_session()
        for item in session.query(News):
            result.append(NewsItemViewModel(item))
        return result

