from lesson3.repositories.Repository import Repository


class HeadHunterRepository(Repository):
    """
    Репозиторий для получения данных с сайта hh.ru
    """

    def __init__(self):
        Repository.__init__(self, 'hh.ru')
        Repository.base_url = 'https://hh.ru/search/vacancy?text='
        Repository.item_class = '.vacancy-serp-item'
        Repository.title_class = '.resume-search-item__name'
        Repository.link_class = '.bloko-link'
        Repository.compensation_class = '.vacancy-serp-item__compensation'
        Repository.payload_key = 'text'
