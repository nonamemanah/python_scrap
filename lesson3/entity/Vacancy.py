from lesson3.entity.Salary import Salary


class Vacancy:
    """
    Вакансия
    """
    def __init__(self, name: str, salary: Salary, link: str, site: str):
        self.__name = name
        self.__salary = salary
        self.__link = link
        self.__site = site

    @property
    def name(self):
        return self.__name

    @property
    def salary(self):
        return self.__salary

    @property
    def link(self):
        return self.__link

    @property
    def site(self):
        return self.__site

    def to_dict(self):
        return {
            "name": self.name,
            "salary": self.salary.to_dict(),
            "link": self.link,
            "site": self.site
        }

    def __repr__(self):
        return f"Наименование: {self.name}. Ссылка: {self.link}. ЗП: {self.salary}. Источник: {self.site}"