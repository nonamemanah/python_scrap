from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

__engine = create_engine('sqlite:///news.db', echo=True)

Base = declarative_base()
class News(Base):
    __tablename__ = 'News'
    __id = Column('id', Integer, primary_key=True, unique=True, autoincrement=True)
    __title = Column('title', String(255))
    __source = Column('source', String(255))
    __link = Column('link', String(255))
    __publication_date = Column('publication_date', String(255))

    def __init__(self, source: str, title: str,  link: str, publication_date: str):
        self.__source = source
        self.__title = title
        self.__link = link
        self.__publication_date = publication_date

    def __repr__(self):
        return f"<User('{self.source}', '{self.title}', '{self.link}', '{self.publication_date}')>"

    @property
    def id(self):
        return self.__id

    @property
    def title(self):
        return self.__title

    @property
    def source(self):
        return self.__source

    @property
    def link(self):
        return self.__link

    @property
    def publication_date(self):
        return self.__publication_date


Base.metadata.create_all(__engine)

