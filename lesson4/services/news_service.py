import typing
from lesson4.Models.news_item_view_model import NewsItemViewModel
from lesson4.entity.news import News
from lesson4.repositories.db_repository import DbRepository
from lesson4.repositories.lenta_repository import LentaRepository
from lesson4.repositories.mail_repository import MailRepository
from lesson4.repositories.yandex_repository import YandexRepository


class NewsService:
    __mail_repository: MailRepository
    __lenta_repository: LentaRepository
    __yandex_repository: YandexRepository
    __db_repository: DbRepository

    def __init__(self):
        self.__mail_repository = MailRepository()
        self.__lenta_repository = LentaRepository()
        self.__yandex_repository = YandexRepository()
        self.__db_repository = DbRepository()

    def sync_news(self):
        '''
        Синхронизация новостей.
        Получение новостей из lenta.ru, mail.ru и yandex.ru
        Производится сохранение в БД всех записей
        :return:
        '''
        items = self.__yandex_repository.collect_data()
        self.__save_items_to_db(items)
        items = self.__mail_repository.collect_data()
        self.__save_items_to_db(items)
        items = self.__lenta_repository.collect_data()
        self.__save_items_to_db(items)

    def get_news(self):
        '''
        Получение списка новостей из БД в видеде списка вьюмоделей
        :return:
        '''
        result = []
        session = self.__db_repository.create_session()
        for item in session.query(News):
            result.append(NewsItemViewModel(item))
        return result

    def __exist(self, title: str):
        '''
        Проверка на существование записи новости в базу данных
        :param title:
        :return:
        '''
        session = self.__db_repository.create_session()
        result = session.query(News).filter(News.title == title).first()
        return result is not None

    def __save_items_to_db(self, items: typing.List[News]):
        '''
        Сохранение новостей в базу данных
        :param items:
        :return:
        '''
        session = self.__db_repository.create_session()
        for item in items:
            if not self.__exist(item.title):
                session.add(item)

        session.commit()
        session.close()


