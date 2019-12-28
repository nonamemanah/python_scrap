from lesson4.entity.news import News


class NewsItemViewModel:
    __title: str
    __source: str
    __link: str
    __publication_date: str

    def __init__(self, news: News):
        self.title = news.title
        self.source = news.source
        self.link = news.link
        self.publication_date = news.publication_date

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, value: str):
        self.__title = value

    @property
    def source(self) -> str:
        return self.__source

    @source.setter
    def source(self, value: str):
        self.__source = value

    @property
    def link(self) -> str:
        return self.__link

    @link.setter
    def link(self, value: str):
        self.__link = value

    @property
    def publication_date(self) -> str:
        return self.__publication_date

    @publication_date.setter
    def publication_date(self, value: str):
        self.__publication_date = value

    def __repr__(self):
        return f"return f'Source: {self.source}; title: {self.title}; link: {self.link}; date: {self.publication_date}"

