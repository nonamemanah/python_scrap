from lesson2.repositories.RabotaRuRepository import RabotaRuRepository
from lesson2.repositories.HeadHunterRepository import HeadHunterRepository


class RepositoryFactory:
    @staticmethod
    def createRepository(type: int):
        """
        Создание репозитория по типу:
        0 - HeadHunter
        1 - superjob.ru
        """
        if type == 0:
            return HeadHunterRepository()
        if type == 1:
            return RabotaRuRepository()

        raise Exception("Тип не поддерживается в этой версии приложения")
