from lesson3.repositories.DatabaseRepository import DatabaseRepository
from lesson3.repositories.RepositoryFactory import RepositoryFactory


class VacancyService:
    def collect(self, name: str):
        repo = RepositoryFactory.createRepository(0)
        result = repo.get_data(name)
        db = DatabaseRepository()
        if len(result) > 0:
            db.add_vacancies(result)

        repo = RepositoryFactory.createRepository(1)
        result = repo.get_data(name)
        if len(result) > 0:
            db.add_vacancies(result)

    def get_by_salary(self, salary: float):
        db = DatabaseRepository()
        return db.get_vacancies(salary)

