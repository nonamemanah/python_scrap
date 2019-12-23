import json
import typing
from pprint import pprint

from pymongo import MongoClient

from lesson3.entity.Salary import Salary
from lesson3.entity.Vacancy import Vacancy


class DatabaseRepository:
    __connection_string = 'mongodb://127.0.0.1:27017'
    __client = MongoClient(__connection_string)
    __db = __client.localhost

    def get_vacancies(self, salary: float):
        result = []
        items = self.__db['vacancies'].find({'salary.start': {'$gt': salary} })
        for item in items:
            vacancy = Vacancy(item['name'], Salary(''), item['link'], item['site'])

            vacancy.salary.start = item['salary']['start']
            vacancy.salary.end = item['salary']['end']

            result.append(vacancy)
        return result

    def add_vacancies(self, items: typing.List[Vacancy]):
        items_for_save = []
        for item in items:
            exist_item = self.__db['vacancies'].find_one({ 'name': item.name })
            if exist_item is None:
                items_for_save.append(item.to_dict())

        if len(items_for_save) > 0:
            self.__db['vacancies'].insert_many(items_for_save)

