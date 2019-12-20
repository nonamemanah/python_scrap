from lesson2.repositories.RepositoryFactory import RepositoryFactory

def app():
    vacancy_name = input('Введите наименование ваканисии: ')
    repo = RepositoryFactory.createRepository(0)
    result = repo.get_data(vacancy_name)
    if len(result) == 0:
        print('Ничего не найдено')

    for item in result:
        print(item)

    repo = RepositoryFactory.createRepository(1)
    result = repo.get_data(vacancy_name)
    if len(result) == 0:
        print('Ничего не найдено')

    for item in result:
        print(item)

if __name__ == '__main__':
    app()
