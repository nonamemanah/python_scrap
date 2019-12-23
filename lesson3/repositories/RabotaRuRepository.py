from lesson3.repositories.Repository import Repository


class RabotaRuRepository(Repository):
    """
        Репозиторий для получения данных с сайта hh.ru
        """

    def __init__(self):
        Repository.__init__(self, 'rabota.ru')
        Repository.base_url = 'https://www.rabota.ru/vacancy/?query='
        Repository.item_class = '.vacancy-preview-card'
        Repository.title_class = '.vacancy-preview-card__title-text'
        Repository.link_class = 'a[itemprop="title"]'
        Repository.compensation_class = '.vacancy-preview-card__salary'
        Repository.payload_key = 'query'
