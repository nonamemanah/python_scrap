from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

class DbRepository:
    __engine = create_engine('sqlite:///news.db', echo=True)
    __base = declarative_base()

    def __init__(self):
        self.__base.metadata.create_all(self.__engine)

    def create_session(self):
        session = sessionmaker(bind=self.__engine)
        return session()

    def get_news(self):
        session = self.__create_session()

