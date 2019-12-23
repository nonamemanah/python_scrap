from lesson3.services.VacancyService import VacancyService

def app():
    vacancy_name = input('Введите наименование ваканисии: ')
    vacancy_service = VacancyService()
    vacancy_service.collect(vacancy_name)

    vacancies = vacancy_service.get_by_salary(120000)
    for item in vacancies:
        print(item)


if __name__ == '__main__':
    app()
