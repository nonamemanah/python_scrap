class News:
    __source: str
    __title: str
    __link: str
    __publication_date: str

    def __init__(self, source: str, title: str, link: str, date: str):
        self.__source = source
        self.__title = title
        self.__link = link
        self.__publication_date = date

    @property
    def source(self) -> str:
        return self.__source

    @property
    def title(self) -> str:
        return self.__title

    @property
    def link(self) -> str:
        return self.__link

    @property
    def publication_date(self) -> str:
        return self.__publication_date

    def __repr__(self):
        return f'Source: {self.source}; title: {self.title}; link: {self.link}; date: {self.publication_date}'


